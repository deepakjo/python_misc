
class ToDictMixin(object):
    def to_dict(self):
        print('Elems in __dict__', self.__dict__)
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            print('key=%s value=%s', key, value)
            output[key] = self._traverse(key, value)
        return output
    
    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            print('ToDictMixin')
            return value.to_dict()
        elif isinstance(value, dict):
            print('dict instance')
            return self._traverse_dict(value)
        elif isinstance(value, list):
            print('list in dict')
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            print('hasattr')
            return self._traverse_dict(value.__dict__)
        else: 
            print('value', value)
            return value    

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent) and key=='parent'):
            return value.value
        else:
            return super()._traverse(key, value)

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)

print(root.to_dict())

import json

class JsonMixin(object):
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        print ('kwargs:', kwargs)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())

class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [Machines(**kwargs) for kwargs in machines]
        print ('Datacenter Init called')

class Switch(ToDictMixin, JsonMixin):
    def __init__(self, ports=None, speed=None):
        print ('Switch Init called', ports, speed)
        self.ports = ports
        self.speed = speed

class Machines(ToDictMixin, JsonMixin):
    def __init__(self, cores=None, ram=None, disk=None):
        print ('Machines Init called', cores, ram, disk)
        self.cores = cores
        self.ram = ram
        self.disk = disk

# Example 11
serialized = """{
    "switch": {"ports": 5, "speed": 1e9},
    "machines": [
        {"cores": 8, "ram": 32e9, "disk": 5e12},
        {"cores": 4, "ram": 16e9, "disk": 1e12},
        {"cores": 2, "ram": 4e9, "disk": 500e9}
    ]
}"""

deserialized = DatacenterRack.from_json(serialized)
roundtrip = deserialized.to_json()
assert json.loads(serialized) == json.loads(roundtrip)


