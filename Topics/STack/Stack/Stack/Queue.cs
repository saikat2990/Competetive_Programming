public class Node
{
    public Node(int value, Node head, Node tail)
    {
        this.value = value;
        Head = head;
        Tail = tail;
    }

    public int value { get; set; }
    public Node Head { get; set; }
    public Node Tail { get; set; }

}

public class Queue
{
    private Node head;
    private Node tail;
    private Node node;

    public Queue()
    {
        head = null;
        tail = null;
        node = null;
    }

    public void Enqueue(int value)
    {
        if (head == null)
        {
            head = new Node(value, null, null);
            node = head;
        }
        else
        {
            var newNode = new Node(value, node, null);
            node.Tail = newNode;
            node = newNode;
        }
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

class Program
{
    public static void Main(string[] args)
    {
        var data = new Queue();
        data.Enqueue(2); data.Enqueue(3);
        data.Enqueue(4); data.Enqueue(5);
        data.Enqueue(6); data.Enqueue(7);
        data.show();
        data.Dequeue();
        Console.WriteLine("Dequeue One Data");
        data.show();
        data.Dequeue();
        Console.WriteLine("Dequeue One Data");
        data.show();
        data.Dequeue();
        Console.WriteLine("Dequeue One Data");
        data.show();
    }
}