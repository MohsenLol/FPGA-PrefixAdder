library verilog;
use verilog.vl_types.all;
entity LadnerFischer32b is
    port(
        A               : in     vl_logic_vector(31 downto 0);
        B               : in     vl_logic_vector(31 downto 0);
        S               : in     vl_logic_vector(32 downto 0)
    );
end LadnerFischer32b;
