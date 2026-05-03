from typing import Dict, List, Optional, Any
# from entity import *
class EntityManager:
    """By Deepseek AI"""
    def __init__(self):
        # 核心数据结构
        self.entities = []  # 列表：用于遍历
        self.entities_by_id = {}  # 字典：用于查找

        # ID计数器
        self._next_id = 0

    def add_entity(self, entity: "Entity") -> int:
        """添加怪物并分配ID"""
        entity.id = self._next_id
        self.entities.append(entity)
        self.entities_by_id[self._next_id] = entity
        self._next_id += 1
        return entity.id

    def get_entity(self, entity_id: int) -> Optional[Any]:
        """通过ID获取怪物"""
        return self.entities_by_id.get(entity_id)

    def remove_entity(self, entity_id: int) -> bool:
        """移除怪物"""
        if entity_id in self.entities_by_id:
            entity = self.entities_by_id[entity_id]
            if entity in self.entities:
                self.entities.remove(entity)
            del self.entities_by_id[entity_id]
            return True
        return False

    def update_all(self):
        """更新所有怪物"""
        for entity in self.entities:
            entity.update()

    def get_all_entities(self) -> List[Any]:
        """获取所有怪物"""
        return self.entities.copy()

    def clear_all(self):
        """清空所有怪物"""
        self.entities.clear()
        self.entities_by_id.clear()
        self._next_id = 0
    

        