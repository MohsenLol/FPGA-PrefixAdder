`timescale 1ns/1ns

module BrentKung32b_rtb;



wire [32 : 0] S;

reg [32 - 1 : 0] A, B;

reg [32 : 0] SR;

BrentKung32b UUT(.A(A), .B(B), .S(S));

integer errors = 0, i = 0;

initial begin

    for (i = 0; i < 100000; i = i + 1) begin

        A = {$random()};

        B = {$random()};

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
