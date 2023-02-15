public class Node 
{
    Records record;
    Node next;

    Node()
    {
        record=new Records();
        next=null;
    }
    Node(int t_id, int t_s_amt, String cname, int cat)
    {
        record=new Records(t_id, t_s_amt, cname, cat);
        next=null;
    }

}
