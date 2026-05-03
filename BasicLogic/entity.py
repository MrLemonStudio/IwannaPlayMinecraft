import storage
from typing import Self,Dict,List,Optional,Any
class Entity:
    def __init__(self, name:str, picture:bytes):
        self.name = name
        self.health:float = 20
        self.damage:float = 1
        self.length:float = 1
        self.height:float = 1
        self.defence:float = 0
        self.can_be_tamed:bool = False
        self.picture = picture
    def attack(self, target:Self)->float:
        target.health -= self.damage*(1-target.defence)
        return target.health
    def heal(self, target:Self,healing_HP:float)->float:
        target.health += healing_HP
        return target.health

class Player(Entity,storage.Storage):
    def __init__(self, name: str, picture: bytes):
        super().__init__(name, picture)
        self.height:float=2

class EntityManager:
    """By Deepseek AI"""
    def __init__(self):
        self.entities_list: List[Entity] = []
        self.entities_dict: Dict[int, Entity] = {}
        self.next_id = 0  
        self.total_created = 0
        self.total_removed = 0
        self.active_count = 0
        self.to_add: List[Entity] = []
        self.to_remove: List[int] = []
    def spawn_entity(self, entity: Entity) -> int:
        entity_id = self.next_id
        self.next_id += 1
        entity.id = entity_id
        self.to_add.append(entity)
        for entity in self.to_add:
            self.entities_list.append(entity)
            self.entities_dict[entity.id] = entity
            self.total_created += 1
        self.to_add.clear()
        for entity_id in self.to_remove:
            if entity_id in self.entities_dict:
                entity = self.entities_dict[entity_id]
                if entity in self.entities_list:
                    self.entities_list.remove(entity)
                del self.entities_dict[entity_id]
                self.total_removed += 1
        self.to_remove.clear()
        self.active_count = len(self.entities_list)
        for entity in self.to_add:
            self.entities_list.append(entity)
            self.entities_dict[entity.id] = entity
            self.total_created += 1
        self.to_add.clear()
        for entity_id in self.to_remove:
            if entity_id in self.entities_dict:
                entity = self.entities_dict[entity_id]
                if entity in self.entities_list:
                    self.entities_list.remove(entity)
                del self.entities_dict[entity_id]
                self.total_removed += 1
        self.to_remove.clear()
        self.active_count = len(self.entities_list)
        return entity_id
    def get_entity(self, entity_id: int) -> Optional[Entity]:
        return self.entities_dict.get(entity_id)
    def mark_for_removal(self, entity_id: int) -> bool:
        if entity_id in self.entities_dict:
            self.to_remove.append(entity_id)
            return True
        return False
    def update_all(self) -> None:
        for entity in self.entities_list:
            raise Exception("There should be the AI of the entity")
            if hasattr(entity, 'hp') and entity.hp <= 0:
                self.mark_for_removal(entity.id)
    def get_all_entities(self) -> List[Entity]:
        return self.entities_list.copy()
    def get_entity_ids(self) -> List[int]:
        return list(self.entities_dict.keys())
    def clear_all(self) -> None:
        self.entities_list.clear()
        self.entities_dict.clear()
        self.to_add.clear()
        self.to_remove.clear()
        self.active_count = 0
    def get_stats(self) -> Dict[str, Any]:
        return {
            'active_count': self.active_count,
            'total_created': self.total_created,
            'total_removed': self.total_removed,
            'pending_add': len(self.to_add),
            'pending_remove': len(self.to_remove),
            'next_id': self.next_id
        }