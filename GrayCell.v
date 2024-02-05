
module GrayCell(PIK,  GIK , GKJ, GIJ);
    input PIK, GIK, GKJ;
    output GIJ;
    wire mid;
    and U0(mid, PIK, GKJ);
    or  U1(GIJ, mid, GIK);

endmodule