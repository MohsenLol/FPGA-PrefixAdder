`timescale 1ns/1ns

module BrentKung32b_etb;

wire [32 : 0] S;

reg [32 - 1 : 0] A, B;

reg [32 : 0] SR;

BrentKung32b UUT(.A(A), .B(B), .S(S));

reg condi, condj;

integer errors = 0;

initial begin

    condi = 1;

    condj = 1;

    A = 0;

    B = 0;

    while(condi) begin

        condj = 1;

        while(condj) begin

            SR = A + B;

            #1;

            if(S !== SR) begin

                errors = errors + 1;

                $display("Missmatch : %dD(%bB) + %dD(%bB) => %dD(%bB) != %dD", A, A, B, B, S, S, SR);

            end 

            B = B + 1;

            if(B == 0) begin

                condj = 0;

            end

        end

        A = A + 1;

        if(A == 0) begin 

            condi = 0;

        end



    end

    $display("Total Error count is %d", errors);

    $stop();

end

endmodule
