module topSISO;//merge acum
    reg[3:0]a;
    wire si,d0,d1,d2,dout;
    wire[3:0] pout;
    reg clk,reset,pl;
    wire check;
    SerialIn Sisul(a,pl,si,check);
    BistabilD D0(si,clk,reset,d0);
    BistabilD D1(d0,clk,reset,d1);
    BistabilD D2(d1,clk,reset,d2);
    BistabilD D3(d2,clk,reset,dout);
    ParalelOut Posul({d0,d1,d2,dout},check,pout);
    initial begin
        a=0;reset=0;clk=0;
        #10 a=6;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #10 pl=1;
        #10 pl=0;
        #100
        $finish();
        
    end
    initial forever #10 clk=~clk;
    
endmodule

module BistabilD(A,clk,reset,out);
  input A,clk,reset;
  output reg out;
  
  always@(posedge clk)begin
    if(reset==1)
      out=0;
    else 
      out<=A;
  end
 	
endmodule

module ParalelOut(A,check,out);
  input[3:0] A;
  input check;
  output reg [3:0] out;
  always@(check)
    if(check==1)
        out<=A;
    else out<=4'bxxxx;
endmodule

module SerialIn(A,clk,out,check);
  input[3:0] A;
  input clk;
  output reg out;
  output check;
  reg[1:0] counter=1'b0;
  always@(posedge clk)begin
    out<=A[counter];
    if(counter<3)
        counter<=counter+1;
    else
        counter<=0;
  end
  assign check=(counter==1);
endmodule
