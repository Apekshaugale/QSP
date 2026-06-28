class Narrowing2
{
public static void main(String[]args)
{

double d1 = 2345.6789d;

//int i1 = (int) d1;
//System.out.print(i1);//2345

//short s1 = (short) d1;
//System.out.print(s1);//2345

//char c1 = (char)d1;
//System.out.print(c1);//?

//byte b1 = (byte) d1;
//System.out.print(b1);//41

float f1 = (float) d1;
System.out.print(f1);//2345.679


}
}