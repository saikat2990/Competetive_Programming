public class Solution
{
    public string GenerateAnswer(string senate)
    {
        Dictionary<string, string> victory = new Dictionary<string, string>();
        victory.Add("R", "Radiant");
        victory.Add("D", "Dire");
        string result = "";
        int RCount = 0;
        int DCount = 0;

        var data = new Queue();
        foreach (var key in senate)
        {
            data.Enqueue(key.ToString());
            if (key.ToString() == "R") RCount++;
            else DCount++;
        }

        while (true)
        {
            var victoryKey = data.GetHeadValue();
            Console.WriteLine(victoryKey + " " + DCount.ToString() + " " + RCount.ToString());
            if (victoryKey == "R")
            {
                DCount -= 1;
                data.Remove("D");
                if (DCount == 0) return "Radiant";
            }

            else
            {
                RCount -= 1;
                data.Remove("R");
                if (RCount == 0) return "Diet";
            }
            data.Dequeue();
            data.Enqueue(victoryKey);
            data.show();
        }
    }

    public string PredictPartyVictory(string senate)
    {
        return GenerateAnswer(senate);
    }
}

class Program1
{
    public static void Main1(string[] args)
    {
        var solution = new Solution();
        var answer = solution.PredictPartyVictory(
            "DDR");
        Console.WriteLine(answer);
    }
}