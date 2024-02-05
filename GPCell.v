module GPCell(A, B, G, P);
    input A, B;
    output G, P;
    and and0(G, A, B);
    xor xor0(P, A, B);
endmodule