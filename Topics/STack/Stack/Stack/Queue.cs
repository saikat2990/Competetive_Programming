public class Node
{
    public Node(string value, Node head, Node tail)
    {
        this.value = value;
        Head = head;
        Tail = tail;
    }

    public string value { get; set; }
    public Node Head { get; set; }
    public Node Tail { get; set; }

}

public class Queue
{
    private Node head;
    private Node tail;

    public Queue()
    {
        head = null;
        tail = null;
    }

    public void Enqueue(string value)
    {
        if (head == null)
        {
            head = new Node(value, null, null);
        }
        else
        {
            var newNode = head;
            while (true)
            {
                if (newNode.Tail != null) newNode = newNode.Tail;
                else break;
            }
            var addedNewNode = new Node(value, newNode, null);
            newNode.Tail = addedNewNode;
        }
    }

    public void Remove(string value)
    {
       var tempQueue = new Queue();
       var currentNode = head;
       int index = 0;
       while (currentNode!=null)
       {
           index++;
            if (currentNode.value == value)
           {
               break;
           }

           
           currentNode = currentNode.Tail;
       }

       int secondIndex = 0;
       currentNode = head;
       var tempNode = new Node("",null,null);
       while (currentNode!=null)
       {
           
           secondIndex++;
           if (index != secondIndex)
           {
               if (tempQueue.head == null)
               {
                   tempNode = new Node(currentNode.value, null, null);
                   tempQueue.head = tempNode;
               }
               else
               {
                   var newNode = new Node(currentNode.value, tempNode, null);
                   tempNode.Tail = newNode;
                   tempNode = newNode;
               }
           }
           currentNode = currentNode.Tail;
       }

       head = tempQueue.head;
       tempQueue=null;
       currentNode= null;
    }

    public Node GetHead()
    {
        return head;
    }

    public string GetHeadValue()
    {
        if (head == null) return "";
        return head.value;
    }

    public void Dequeue()
    {
        if (head == null)
        {
            Console.WriteLine("No Head Available");
            return;
        }

        head = head.Tail;
    }

    public void show()
    {
        var iterator = head;
        while (iterator != null)
        {
            Console.WriteLine(iterator.value);
            iterator = iterator.Tail;
        }
    }
}

//partial class Program1
//{
//    public static void Main1(string[] args)
//    {
//        var data = new Queue();
//        data.Enqueue(2); data.Enqueue(3);
//        data.Enqueue(4); data.Enqueue(5);
//        data.Enqueue(6); data.Enqueue(7);
//        data.show();
//        data.Dequeue();
//        Console.WriteLine("Dequeue One Data");
//        data.show();
//        data.Dequeue();
//        Console.WriteLine("Dequeue One Data");
//        data.show();
//        data.Dequeue();
//        Console.WriteLine("Dequeue One Data");
//        data.show();
//    }
//}