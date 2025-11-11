internal class Program
{
    public class TestClass
    {
        int _testField;
        public void TestMethod()
        {
            Console.WriteLine($"Test Field Value: {_testField}!");
        }
    }
    private static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}