module topSISO;//nu merge
    reg[3:0]a;
    wire si,d0,d1,d2,dout;
    reg clk,reset,pl;
    SerialIn Sisul(a,pl,si);
    BistabilD D0(si,pl,clk,reset,d0);
    BistabilD D1(d0,pl,clk,reset,d1);
    BistabilD D2(d1,pl,clk,reset,d2);
    BistabilD D3(d2,pl,clk,reset,dout);
    initial begin
        a=0;reset=0;clk=0;pl=0;
        
        #10
        a=5;
        #4
        pl=1;
        #5 
        pl=0;
        #5
        pl=1;
        #5
        pl=0;
        #5
        pl=1;
        #5
        pl=0;
        #5
        pl=1;
        #5
        pl=0;
        #5
        pl=1;
        #5
        pl=0;
        #100
        $finish();
        forever #10 clk=~clk;
    end
    
    
endmodule

module BistabilD(A,pl,clk,reset,out);
  input A,clk,reset,pl;
  output reg out;
  
  always@(posedge clk)begin
    if(reset==1)
      out=0;
    else 
    if(pl==1)
      out<=A;
  end
 	
endmodule

module ParalelIn(A,clk,out);
  input[3:0] A;
  input clk;
  output reg [3:0] out;
  
endmodule

module SerialIn(A,clk,out);
  input[3:0] A;
  input clk;
  output reg out;
  reg[1:0] counter=1'b0;
  always@(posedge clk)begin
    out<=A[counter];
    if(counter<3)
        counter<=counter+1;
    else
        counter<=0;
  end
endmodule
