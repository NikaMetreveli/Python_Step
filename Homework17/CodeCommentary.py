##linked_list.py

#vqmnit node class -s, romelsag gadavcemt raime monacems da init metodid data cvlads vadzlebt am datis mnishvnelobas
#xolo am node is shemdeg mnishvnelobas vadzlebt none-s radgan jer ar vicit
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#vqmnit linkedlist class da vuwert sxvadasxva metodebs
class LinkedList:
    def __init__(self):
        self.head = None

    #gadacemul data-s amatebs node-shi da svams listis bolo poziciaze
    def append(self, data):
        new_node = Node(data)
        #tu listshi monacemi jer ar arsebobs, gadacemul nodes amatebs pirvel wevrad
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        #tu listi aqamde ar iyo carieli, miyveba pirveli node-dan da amowmebs iqamde sanam ar miva iset node-ze, romelsac ar aqvs monacemi da mere amatebs axal nodes
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    #listshi edzebs gadacemul indexze mdgom monacems da shlis
    def remove_at(self, index):
        #tu gadacemuli indexi naklebia 0-ze da listshi ar aris monacemi, funqcia arafers aketebs
        if index < 0 and self.head is None:
            return
        #tu indexia 0, anu unda amoishalos listis pirveli monacemi, listis head node ad vxdit am listis meore wevrs
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_position = 0

        #iwyebs pirveli node dan da sanam ar miadgeba im nodes, romelic aris gadacemuli index - 1 poziciaze, manamde cvlis current_node is mnishvnelobas da 1-it zrdis curren_positions
        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1
        # rodesac ipovis shesabamis nodes, am nodeis adgilas dgams mis shemdeg indexze mjdom nodes, xolo bolos naxsenebi node is adgilas, washlili nodeisgan 2 indexit shemdeg arsebul nodes svams
        if current_node.next:
            current_node.next = current_node.next.next

    # bechdavs chvens lists
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next


linked_list = LinkedList()

linked_list.append(10)
linked_list.append(5)
linked_list.append(25)
linked_list.append(12)
linked_list.append(11)

linked_list.display()
print()
linked_list.remove_at(2)
linked_list.display()
print()
linked_list.remove_at(2)
linked_list.display()

#stack.py

#vqmnit Stack class da shignit vadefinebt metodebs
class Stack:
    # tavidan monacemi ar gvaq, amitom bolo monacemis mnishvneloba iqneba none xolo stackis sigrdze 0
    def __init__(self):
        self.top_node = None
        self.length = 0

    # amowmebs aris tu ara stacki carieli, misi sigrdzis shemowmebit
    def empty(self):
        return self.length == 0

    # gvibrunebs stackis sigrdzes
    def size(self):
        return self.length

    # stekis tavshi amatebs axal nodes node klasis gamoyenebit, shemdeg top_node cvlads adzlevs am axali nodes is mnishvnelobas,
    # xolo mis damatebamde romelic iyo top node imas adzlevs axlis shemdegi node is mnishvnelobas da zrdis stekis sigrdzes 1 it
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    # tu steki araa carieli, am stekidan agdebs bolo damatebul nodes da abrunebs mis mnishvnelobas. amistvis amogdebuli monacemis cvlads anichebs bolos damatebuli node is mnishvnelobas
    # shemdeg, stack klasis top_node cvlads anichebs amogdebamde me2 node is mnishvnelobas da amcirebs sigrdzes 1 it 
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError('Stack is empty')


stack = Stack()
# print(stack.empty())
# print(stack.size())

stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
# print(stack.empty())
# print(stack.size())


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.empty())
# print(stack.size())