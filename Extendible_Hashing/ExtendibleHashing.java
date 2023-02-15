import java.io.File;
import java.io.*;
import java.util.Hashtable;
import java.util.Scanner;

public class ExtendibleHashing
{
    int MAX_FILE_SIZE;
    int MAX_BUCKET_SIZE;
    int max_digits_in_hash;

    String output_holder; 

    public int GD;
    public Records allRecords[];
    public Hashtable<String, Integer> BAT = new Hashtable<>(); //Bucket Addressing Table
    public Bucket secondary_memory[]; //used for simulated secondary memory
    public int next_bucket_slot_ptr; //pointer to the slot in secondary that can be used for the next bucket creation
    public int next_overflow_bucket_ptr;

    ExtendibleHashing(int max_size, int buck_size, int hash_digit)
    {
        //fixing the inputs
        MAX_FILE_SIZE=max_size;
        MAX_BUCKET_SIZE=buck_size;
        max_digits_in_hash = hash_digit;

        output_holder=""; 

        GD=0;
        allRecords = new Records[MAX_FILE_SIZE];
        secondary_memory = new Bucket[100000];
        next_overflow_bucket_ptr=MAX_BUCKET_SIZE+1;
        secondary_memory[0] = new Bucket(max_size, buck_size, hash_digit);
        next_bucket_slot_ptr=1;
    }

    /*READ RECORDS FROM FILE*/
    public void readRecords() throws FileNotFoundException
    {
        Scanner dataset_Reader=new Scanner(new File("dataset.txt"));
        String temp1="", temp2=""; //temp1 is used to store the entire record, temp2 is used tyo sotre individual entries of that record
        String columns[]=new String[4]; //strings to hold the individual column values on a temporary basis before conversion
        int len_temp1;
        int current_column=0;
        int current_record=0;
        while(dataset_Reader.hasNextLine())
        {
            temp1=dataset_Reader.nextLine();
            len_temp1=temp1.length();
            current_column=0;
            for(int i=0; i<len_temp1; i++)
            {
                if(temp1.charAt(i)==',')
                {
                    columns[current_column++]=temp2;
                    temp2="";
                }
                else
                    temp2+=temp1.charAt(i);
            }
            columns[current_column]=temp2;
            temp2="";
    
            Records temp_Record= new Records(Integer.parseInt(columns[0]), Integer.parseInt(columns[1]), columns[2], Integer.parseInt(columns[3]));
            allRecords[current_record++] =temp_Record;

        }
    }
    
    /*PROVIDES BINARY VALUE OF SOME INTEGER UP TO GD DIGITS*/
    public String find_Binary_Value(int n, int digits)
    {
        String res="";
        int count=0;
        if(digits<0)
            digits=0;
        //int max_count_value=(int)Math.pow(2,GD_val);
        while(count<digits)
        {
            res=n%2+res;
            n=n/2;
            count++;
        }
        return res;
    }

    /*EXPANDS HASH TABLE*/
    public void modify_hash_table()
    {
        int number_of_possible_hashes = (int) Math.pow(2, GD);
        String hash_val = "";
        int ptr_to_secondary_memory=0;

        for(int i=0; i<number_of_possible_hashes; i++)
        {
            hash_val = find_Binary_Value(i, GD);
            if(GD==0)
                ptr_to_secondary_memory = 0;
            
            else
                ptr_to_secondary_memory = BAT.get(hash_val);

            if(GD!=0)
                BAT.remove(hash_val);
            BAT.put(hash_val+"0", ptr_to_secondary_memory);
            BAT.put(hash_val+"1", ptr_to_secondary_memory);
        }
        GD++;
        output_holder+="Global depth increased to "+GD+".\n";
        output_holder+="*********BAT expansion complete. Buckets are as follows:*********\n\n";
        System.out.println("Global depth increased to "+GD+".");
        System.out.println("*********BAT expansion complete. Buckets are as follows:*********\n");
        printfunction(); //print buckets after BAT expansion
    }

    /*THIS DOES REHASHING FOR THE BUCKET SPECIFIED*/
    public void rehash_function(int index_of_bucket_to_be_rehashed, int index_of_new_bucket, int record_index_in_allRecords)
    {
        //this loop's purpose is to update the whole chain's elements_in_the original splitting buckets value
        secondary_memory[index_of_bucket_to_be_rehashed].elements_in_bucket = find_elements_in_bucket(index_of_bucket_to_be_rehashed);

        int number_of_records_in_split_bucket = secondary_memory[index_of_bucket_to_be_rehashed].elements_in_bucket + 1;

        //there is a guarantee that overflow bucket is also full if splitBucket is invoked -> Following code is based on that assumption

        Records temp_rehash_holder[] = new Records[number_of_records_in_split_bucket];
        int current_bucket_index = index_of_bucket_to_be_rehashed;
        int j;

        for(int i=0; i<number_of_records_in_split_bucket; i++)
        {
            j=0;
            Bucket current_bucket = secondary_memory[current_bucket_index];
            while(i<number_of_records_in_split_bucket && j<current_bucket.next_free_space_ptr)
            {
                temp_rehash_holder[i++]=current_bucket.bucket_records[j++];
            }
            i--;
            if(current_bucket.has_next_bucket==true)
            current_bucket_index = current_bucket.next_bucket_pointer;
        }
        temp_rehash_holder[number_of_records_in_split_bucket-1]=allRecords[record_index_in_allRecords]; //insert final record to the rehash_holder

        //also adds to the chain if necessary
        //remove links to the older bucket and chains
        secondary_memory[index_of_bucket_to_be_rehashed].flush_bucket();

        for(int i=0; i<number_of_records_in_split_bucket;i++)
        {
            String hash_of_record = find_Binary_Value(temp_rehash_holder[i].trans_id, max_digits_in_hash).substring(0, GD);
            int dest_bucket = BAT.get(hash_of_record);

            int response_code = secondary_memory[dest_bucket].Add_Record(secondary_memory, temp_rehash_holder[i]);
            if(response_code==1) //AddRecords handles the case where chain has been created and insertion happens there
            {
                output_holder+="Record "+i+" with transaction ID "+temp_rehash_holder[i].trans_id+" successfully added to bucket "+dest_bucket+" after rehashing.\n";
                System.out.println("Record "+i+" with transaction ID "+temp_rehash_holder[i].trans_id+" successfully added to bucket "+dest_bucket+" after rehashing.");
            }
            else if(response_code==0) //chaining
            {
                secondary_memory[next_bucket_slot_ptr]= new Bucket(MAX_FILE_SIZE, MAX_BUCKET_SIZE, max_digits_in_hash);
                //change dest_bucket to point to the last bucket in the chain
                while(secondary_memory[dest_bucket].has_next_bucket==true)
                    dest_bucket=secondary_memory[dest_bucket].next_bucket_pointer;
                secondary_memory[dest_bucket].has_next_bucket=true;
                secondary_memory[dest_bucket].next_bucket_pointer = next_bucket_slot_ptr++;
                i--; //reattempt to insert the record
            }
        }

        output_holder+="*********Rehashing complete. Buckets are as follows:*********\n\n";
        System.out.println("*********Rehashing complete. Buckets are as follows:*********\n");
        printfunction(); //print buckets after rehashing
        output_holder+="\n";
        System.out.println();

    }

    /*THIS IS USED TO UPDATE THE NUBMER OF ELEMENTS IN THE FIRST BUCKET OF THE CHAIN*/
    public int find_elements_in_bucket(int index_of_bucket_to_be_traversed)
    {
        int elements_in_bucket=0;
        int dest_bucket = index_of_bucket_to_be_traversed;
        while(secondary_memory[dest_bucket].has_next_bucket==true)
        {
            elements_in_bucket+=MAX_BUCKET_SIZE;
            dest_bucket = secondary_memory[dest_bucket].next_bucket_pointer;
        }
        elements_in_bucket+=secondary_memory[dest_bucket].next_free_space_ptr;
        return elements_in_bucket;
    }

    /*THIS SPLITS THE BUCKET SPECIFIED*/
    public void splitBucket(int index_of_bucket_to_be_split, int record_index_in_allRecords)
    {
        int local_depth = secondary_memory[index_of_bucket_to_be_split].LD;
        int difference_in_gd_and_ld = GD - local_depth;

        int no_of_comb  = (int)Math.pow(2, difference_in_gd_and_ld-1); //we do -1 so that the bit just after LD remains in our control -> This is used to assign new bucket to the bucket which is (LD)1(...), and odler bucket remains with (LD)0(...)
        String combinations[] = new String[no_of_comb];
        for(int i= 0; i< no_of_comb; i++)
            combinations[i]=find_Binary_Value(i, difference_in_gd_and_ld-1);

        String hash_from_local_depth = find_Binary_Value(allRecords[record_index_in_allRecords].trans_id, max_digits_in_hash).substring(0,local_depth);  //The LD in (LD)1(...)
        secondary_memory[next_bucket_slot_ptr]= new Bucket(MAX_FILE_SIZE, MAX_BUCKET_SIZE, max_digits_in_hash);
        for(int i= 0; i< no_of_comb; i++)
            BAT.put(hash_from_local_depth+"1"+combinations[i], next_bucket_slot_ptr);

        //update the LD of both buckets
        secondary_memory[next_bucket_slot_ptr].LD = ++secondary_memory[index_of_bucket_to_be_split].LD;

        rehash_function(index_of_bucket_to_be_split, next_bucket_slot_ptr++, record_index_in_allRecords);
    }

    /*THIS IS THE PRINT FUNCTION WHICH PRINTS THE BAT AND THE CORRESPONDING BUCKETS*/
    public void printfunction()
    {
        int no_of_comb = (int)Math.pow(2, GD);
        for(int i=0; i<no_of_comb; i++)
        {
            String bucket_index_in_string = BAT.get(find_Binary_Value(i, GD))+"";
            int bucket_index;
            if(GD==0)
                bucket_index = 0;
            else
                bucket_index= Integer.parseInt(bucket_index_in_string);

            boolean next_bucket_in_chain_exists = secondary_memory[bucket_index].has_next_bucket;
            output_holder+=find_Binary_Value(i, GD)+"{"+secondary_memory[bucket_index]+"}:\t";
            System.out.print(find_Binary_Value(i, GD)+"{"+secondary_memory[bucket_index]+"}:\t");
            while(next_bucket_in_chain_exists==true)
            {
                output_holder+= secondary_memory[bucket_index].Print_Bucket(GD);
                output_holder+=" => ";
                System.out.print(" => ");
                bucket_index=secondary_memory[bucket_index].next_bucket_pointer;
                next_bucket_in_chain_exists = secondary_memory[bucket_index].has_next_bucket;
            }
            output_holder+= secondary_memory[bucket_index].Print_Bucket(GD);
            output_holder+="\n";
            System.out.println();
        }
    }
    
    /*THIS IS THE MASTER FUNCTION FOR THE ENTIRE PROGRAM*/
    public String extendibleHashing()
    {
        for(int i=0 ;i<MAX_FILE_SIZE; i++)
        {
            Records current_record = allRecords[i];
            output_holder+="\n----------------------Current Record ID = "+allRecords[i].trans_id+"----------------------\n";
            System.out.println("\n----------------------Current Record ID = "+allRecords[i].trans_id+"----------------------");
            String hash_of_record = find_Binary_Value(current_record.trans_id, max_digits_in_hash).substring(0, GD);
            String result_of_hash_search = BAT.get(hash_of_record)+"";
            int secondary_memory_index =0;

            if(GD==0) //GD=0 case
                secondary_memory_index = 0;
            else
                secondary_memory_index = Integer.parseInt(result_of_hash_search);
            
            int response_code = secondary_memory[secondary_memory_index].Add_Record(secondary_memory, current_record); //this also handles overflow bucket not being full
            if(response_code==1)
            {
                output_holder+="Record "+i+" with transaction ID "+allRecords[i].trans_id+" successfully added to bucket "+secondary_memory_index+"\n";
                System.out.println("Record "+i+" with transaction ID "+allRecords[i].trans_id+" successfully added to bucket "+secondary_memory_index);
                printfunction();
            }
            else if(response_code==0)
            {
                if(secondary_memory[secondary_memory_index].LD==GD)
                {
                    output_holder+="Hash Table expansion is needed.\n";
                    System.out.println("Hash Table expansion is needed.");
                    modify_hash_table();
                    i--; //same record will attempt to insert again
                }
                else //if it reaches here, then overflow bucket is also full
                {
                    output_holder+="Split of bucket "+secondary_memory_index+" is needed.\n";
                    System.out.println("Split of bucket "+secondary_memory_index+" is needed.");
                    splitBucket(secondary_memory_index, i);
                }
            }
            else
            {
                output_holder+="Record "+i+" with transaction ID "+allRecords[i].trans_id+" addition has run into some unexpected trouble.\n";
                System.out.println("Record "+i+" with transaction ID "+allRecords[i].trans_id+" addition has run into some unexpected trouble.");
                System.exit(0);
            } 
        }
        output_holder+="\n\n-----------------FINAL OUTPUT-----------------\n\n";
        System.out.println("\n\n-----------------FINAL OUTPUT-----------------\n");
        printfunction();
        output_holder+="\nGlobal Depth: "+GD+"\n";
        output_holder+="\n\n-----------------END OF EXECUTION-----------------";
        System.out.println("\n-----------------END OF EXECUTION-----------------");
        return output_holder;
    }
}
