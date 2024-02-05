library verilog;
use verilog.vl_types.all;
entity rippleCarry8b is
    port(
        A               : in     vl_logic_vector(7 downto 0);
        B               : in     vl_logic_vector(7 downto 0);
        S               : out    vl_logic_vector(8 downto 0)
    );
end rippleCarry8b;
