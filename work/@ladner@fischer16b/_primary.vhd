library verilog;
use verilog.vl_types.all;
entity LadnerFischer16b is
    port(
        A               : in     vl_logic_vector(15 downto 0);
        B               : in     vl_logic_vector(15 downto 0);
        S               : out    vl_logic_vector(16 downto 0)
    );
end LadnerFischer16b;
