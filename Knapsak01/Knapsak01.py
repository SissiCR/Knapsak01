
from queue import Queue
import copy
import time
import copy

class Item:
  def __init__(self, id, benefit, weight):
    self.id = id
    self.benefit = benefit
    self.weight = weight

class Knapsak:
   
    def __init__(self, maxWeight):
        self.maxWeight = maxWeight
        self.currentWeight = 0
        self.currentBenefit = 0
        self.items = [] 
        self.level = 0
        
    def isWeightExceeded(self):
        if self.currentWeight >= self.maxWeight:
            return True
        return False

    def isMaxWeight(self):
        if self.currentWeight == self.maxWeight:
            return True
        return False

    def addItem(self, item):
        self.items.append(item)
        self.currentBenefit = self.currentBenefit + item.benefit
        self.currentWeight =  self.currentWeight + item.weight

    def increaseLevel(self):
       self.level = self.level + 1
 
    def printInfo(self):
        print('**Knapsak Information:**')
        print('Weight:',  self.currentWeight)
        print('Benefit:', self.currentBenefit)
        print('The amount of items stored is:', len(self.items))
        j = 1
        for x in self.items: 
                print('Item', j,':', x.id,  x.benefit,  x.weight)
                j = j + 1
    

class Tree:
    def _init_(self):
        self.bestBenefit = None
        self.queue = None 
        self.stack = None

    def bfSearch(self, items, maxWeight):
        self.queue = Queue(0)
        currentNode = None
    
        if currentNode is None:
            currentNode = Knapsak(maxWeight) 
            self.createChildNodes(currentNode, items[0])
            self.bestBenefit = currentNode  
       
        while self.queue.empty() == False:   
            currentNode = self.queue.get()
            if currentNode.isWeightExceeded() == True:
               continue
            if currentNode.isMaxWeight() == True:
               self.setBestBenefit(currentNode)
               continue
            else:
               self.setBestBenefit(currentNode)
               if currentNode.level <= len(items) - 1:
                 nextItem = items[currentNode.level]
                 self.createChildNodes(currentNode, nextItem)
      
  
    def createNodeCopy(self, node):
        newNode = Knapsak(node.maxWeight)
        newNode.level = node.level
        newNode.items = node.items.copy()
        newNode.currentBenefit = node.currentBenefit
        newNode.currentWeight = node.currentWeight
        return newNode

    def createChildNodes(self, knapsak, item):     
        leftNode = self.createNodeCopy(knapsak) 
        rightNode = self.createNodeCopy(knapsak) 
        leftNode.addItem(item) 
        leftNode.increaseLevel()
        rightNode.increaseLevel()
        self.queue.put(leftNode)
        self.queue.put(rightNode)
        #leftNode = copy.deepcopy(knapsak)
        #rightNode = copy.deepcopy(knapsak)
              
    def setBestBenefit(self, knapsak):
        if knapsak.currentBenefit > self.bestBenefit.currentBenefit:
            self.bestBenefit = knapsak

    def dfSearch(self, items, maxWeight):
        self.stack = []
        currentNode = None
    
        if currentNode is None:
            currentNode = Knapsak(maxWeight) 
            self.createChildN(currentNode, items[0])
            self.bestBenefit = currentNode  
       
        while len(self.stack) > 0:   
            currentNode = self.stack.pop()
            if currentNode.isWeightExceeded() == True:
               continue
            if currentNode.isMaxWeight() == True:
               self.setBestBenefit(currentNode)
               continue
            else:
               self.setBestBenefit(currentNode)
               if currentNode.level <= len(items) - 1:
                 nextItem = items[currentNode.level]
                 self.createChildN(currentNode, nextItem)
        return

    def createChildN(self, knapsak, item):     
        leftNode = self.createNodeCopy(knapsak) 
        rightNode = self.createNodeCopy(knapsak) 
        leftNode.addItem(item) 
        leftNode.increaseLevel()
        rightNode.increaseLevel()
        self.stack.append(rightNode)
        self.stack.append(leftNode)
        


def main():
    allItems = []
    maxWeight = 420
    knapsak = Knapsak(maxWeight)

    def retrieveItemsFromFile():
        with open("knapsakInst.txt", "r") as knapsakInfo:
            content = knapsakInfo.read().splitlines()
            i = content.index('ID b w') + 1
            j = 0
            for x in range(i, len(content) - 1):
                itemInfo = content[x].split() 
                allItems.insert(j, Item(int(itemInfo[0]), int(itemInfo[1]), int(itemInfo[2]))) # for each line create an object item
                j = j + 1 
        
    retrieveItemsFromFile()
    root = Tree()

    t = time.process_time()
    root.bfSearch(allItems, maxWeight)
    elapsedTime = time.process_time() - t
    print('Time for BFS is:', elapsedTime)
    root.bestBenefit.printInfo()
    print('....................................................')
    startTime = time.process_time()
    root.dfSearch(allItems, maxWeight)
    totalTime = time.process_time() - startTime
    print('Time for DFS is:', totalTime)
    root.bestBenefit.printInfo()

    
if __name__=="__main__": 
    main() 

            
