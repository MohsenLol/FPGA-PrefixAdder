library verilog;
use verilog.vl_types.all;
entity rippleCarry is
    port(
        A               : in     vl_logic_vector(1 downto 0);
        B               : in     vl_logic_vector(1 downto 0);
        S               : in     vl_logic_vector(2 downto 0)
    );
end rippleCarry;
