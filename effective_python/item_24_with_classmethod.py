import os
from tempfile import mkdtemp, mkstemp, TemporaryFile
from threading import Thread

class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError
        
class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        print('data_dir', config)
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            if (os.path.isdir(name)):
                continue
        
            print ('name', name)
            yield cls(os.path.join(data_dir, name))

class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        print ('input_data', input_data)
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError
       
    @classmethod
    def create_workers(cls, input_class, config):
        workers = []

        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))

        return workers

class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

class ClassCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('class ')
        print ('no of class', self.result)

    def reduce(self, other):
        self.result += other.result

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))

    return workers

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    
    return first.result

def mapreduce(worker_class, input_class, data_dir):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

config = {'data_dir': '/home/deepak/python/effective_python'}
result = mapreduce(LineCountWorker, PathInputData, config)
print('there are ', result, ' lines')
result = mapreduce(ClassCountWorker, PathInputData, config)
print('there are ', result, ' classes')
