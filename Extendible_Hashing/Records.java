public class Records
{
    public int trans_id;
    public int trans_sale_amt;
    public String customer_name;
    public int item_category;
    Records()
    {
        trans_id=0;
        trans_sale_amt=0;
        customer_name="";
        item_category=0;
    }
    Records(int t_id, int t_s_amt, String cname, int cat)
    {
        trans_id=t_id;
        trans_sale_amt=t_s_amt;
        customer_name=cname;
        item_category=cat;
    }
    @Override
    public String toString() {
        
        String str = "";
        str=trans_id+","+trans_sale_amt+","+customer_name+","+item_category;
        return str;
    }
}