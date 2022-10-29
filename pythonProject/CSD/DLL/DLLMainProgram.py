import double_link_litst as dll

my_dll = dll.DoubleLinkedList()

my_dll.addTail('10')
my_dll.addTail('5')
my_dll.addTail('20')
my_dll.addHead('1')
my_dll.addHead('2')
my_dll.addHead('3')

my_dll.traversal()

my_dll.removeHead()
my_dll.removeHead()

print('\n')

my_dll.removeTail()
my_dll.removeTail()

my_dll.traversal()