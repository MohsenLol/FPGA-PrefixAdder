`timescale 1ns/1ns
module testbench;

wire [_N_ : 0] S;
reg [_N_ - 1 : 0] A, B;
reg [_N_ : 0] SR;
_X_ UUT(.A(A), .B(B), .S(S));
integer errors = 0, i = 0;
initial begin
    for (i = 0; i < _T_; i = i + 1) begin
        A = {_R_};
        B = {_R_};
        SR = A + B;
        #1;
        if(S !== SR) begin
                errors = errors + 1;
                $display("Missmatch : %dD(%bB) + %dD(%bB) => %dD(%bB) != %dD", A, A, B, B, S, S, SR);
        end 
    end
    $display("Total Error count is %d", errors);
    $stop();
end

endmodule