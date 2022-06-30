// See https://aka.ms/new-console-template for more information

using System.Collections;

public interface NestedInteger
{
    bool IsInteger();
    int GetInteger();
    IList<NestedInteger> GetList();
}

public class NestedIterator
{
    private IList<int> result { get; set; }
    private int index { get; set; }

    public NestedIterator(IList<NestedInteger> nestedList)
    {
        result = new List<int>();
        index = 0;
        AddValue(nestedList);
    }

    public void AddValue(IList<NestedInteger> nestedList)
    {
        foreach (var list in nestedList)
        {
            if (list.IsInteger())
            {
                result.Add(list.GetInteger());
            }
            else
            {
                AddValue(list.GetList());
            }
        }
    }

    public bool HasNext()
    {
        return index < result.Count;
    }

    public int Next()
    {
        return result[index++];
    }
}