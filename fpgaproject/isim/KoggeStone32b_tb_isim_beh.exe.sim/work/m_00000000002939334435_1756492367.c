/**********************************************************************/
/*   ____  ____                                                       */
/*  /   /\/   /                                                       */
/* /___/  \  /                                                        */
/* \   \   \/                                                       */
/*  \   \        Copyright (c) 2003-2009 Xilinx, Inc.                */
/*  /   /          All Right Reserved.                                 */
/* /---/   /\                                                         */
/* \   \  /  \                                                      */
/*  \___\/\___\                                                    */
/***********************************************************************/

/* This file is designed for use with ISim build 0x7708f090 */

#define XSI_HIDE_SYMBOL_SPEC true
#include "xsi.h"
#include <memory.h>
#ifdef __GNUC__
#include <stdlib.h>
#else
#include <malloc.h>
#define alloca _alloca
#endif
static const char *ng0 = "C:/Users/Dr.Fly/Desktop/FPGAAdders/KoggeStone32b_tb.v";
static int ng1[] = {0, 0};
static int ng2[] = {2, 0};
static int ng3[] = {16, 0};
static int ng4[] = {1, 0};
static const char *ng5 = "Missmatch : %dD(%bB) + %dD(%bB) => %dD(%bB) != %dD";
static const char *ng6 = "Total Error count is %d";



static void Initial_15_0(char *t0)
{
    char t7[8];
    char t8[8];
    char *t1;
    char *t2;
    char *t3;
    char *t4;
    char *t5;
    char *t6;
    char *t9;
    unsigned int t10;
    unsigned int t11;
    unsigned int t12;
    unsigned int t13;
    unsigned int t14;
    char *t15;
    char *t16;
    char *t17;
    char *t18;
    char *t19;
    char *t20;
    char *t21;
    char *t22;
    char *t23;
    char *t24;
    char *t25;
    char *t26;
    char *t27;

LAB0:    t1 = (t0 + 3328U);
    t2 = *((char **)t1);
    if (t2 == 0)
        goto LAB2;

LAB3:    goto *t2;

LAB2:    xsi_set_current_line(15, ng0);

LAB4:    xsi_set_current_line(19, ng0);
    xsi_set_current_line(19, ng0);
    t2 = ((char*)((ng1)));
    t3 = (t0 + 1768);
    xsi_vlogvar_assign_value(t3, t2, 0, 0, 32);

LAB5:    t2 = (t0 + 1768);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng2)));
    t6 = ((char*)((ng3)));
    memset(t7, 0, 8);
    xsi_vlog_signed_power(t7, 32, t5, 32, t6, 32, 1);
    memset(t8, 0, 8);
    xsi_vlog_signed_less(t8, 32, t4, 32, t7, 32);
    t9 = (t8 + 4);
    t10 = *((unsigned int *)t9);
    t11 = (~(t10));
    t12 = *((unsigned int *)t8);
    t13 = (t12 & t11);
    t14 = (t13 != 0);
    if (t14 > 0)
        goto LAB6;

LAB7:    xsi_set_current_line(41, ng0);
    t2 = (t0 + 2408);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    xsi_vlogfile_write(1, 0, 0, ng6, 2, t0, (char)119, t4, 32);

LAB1:    return;
LAB6:    xsi_set_current_line(19, ng0);

LAB8:    xsi_set_current_line(21, ng0);
    xsi_set_current_line(21, ng0);
    t15 = ((char*)((ng1)));
    t16 = (t0 + 1928);
    xsi_vlogvar_assign_value(t16, t15, 0, 0, 32);

LAB9:    t2 = (t0 + 1928);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng2)));
    t6 = ((char*)((ng3)));
    memset(t7, 0, 8);
    xsi_vlog_signed_power(t7, 32, t5, 32, t6, 32, 1);
    memset(t8, 0, 8);
    xsi_vlog_signed_less(t8, 32, t4, 32, t7, 32);
    t9 = (t8 + 4);
    t10 = *((unsigned int *)t9);
    t11 = (~(t10));
    t12 = *((unsigned int *)t8);
    t13 = (t12 & t11);
    t14 = (t13 != 0);
    if (t14 > 0)
        goto LAB10;

LAB11:    xsi_set_current_line(19, ng0);
    t2 = (t0 + 1768);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng4)));
    memset(t7, 0, 8);
    xsi_vlog_signed_add(t7, 32, t4, 32, t5, 32);
    t6 = (t0 + 1768);
    xsi_vlogvar_assign_value(t6, t7, 0, 0, 32);
    goto LAB5;

LAB10:    xsi_set_current_line(21, ng0);

LAB12:    xsi_set_current_line(23, ng0);
    t15 = (t0 + 1768);
    t16 = (t15 + 56U);
    t17 = *((char **)t16);
    t18 = (t0 + 1448);
    xsi_vlogvar_assign_value(t18, t17, 0, 0, 32);
    xsi_set_current_line(23, ng0);
    t2 = (t0 + 1928);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t0 + 1608);
    xsi_vlogvar_assign_value(t5, t4, 0, 0, 32);
    xsi_set_current_line(23, ng0);
    t2 = (t0 + 3136);
    xsi_process_wait(t2, 1000LL);
    *((char **)t1) = &&LAB13;
    goto LAB1;

LAB13:    xsi_set_current_line(25, ng0);
    t2 = (t0 + 1048U);
    t3 = *((char **)t2);
    t2 = (t0 + 2088);
    xsi_vlogvar_assign_value(t2, t3, 0, 0, 32);
    xsi_set_current_line(27, ng0);
    t2 = (t0 + 1768);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t0 + 1928);
    t6 = (t5 + 56U);
    t9 = *((char **)t6);
    memset(t7, 0, 8);
    xsi_vlog_signed_add(t7, 32, t4, 32, t9, 32);
    t15 = (t0 + 2248);
    xsi_vlogvar_assign_value(t15, t7, 0, 0, 32);
    xsi_set_current_line(29, ng0);
    t2 = (t0 + 2088);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t0 + 2248);
    t6 = (t5 + 56U);
    t9 = *((char **)t6);
    memset(t7, 0, 8);
    xsi_vlog_signed_case_noteq(t7, 32, t4, 32, t9, 32);
    t15 = (t7 + 4);
    t10 = *((unsigned int *)t15);
    t11 = (~(t10));
    t12 = *((unsigned int *)t7);
    t13 = (t12 & t11);
    t14 = (t13 != 0);
    if (t14 > 0)
        goto LAB14;

LAB15:
LAB16:    xsi_set_current_line(21, ng0);
    t2 = (t0 + 1928);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng4)));
    memset(t7, 0, 8);
    xsi_vlog_signed_add(t7, 32, t4, 32, t5, 32);
    t6 = (t0 + 1928);
    xsi_vlogvar_assign_value(t6, t7, 0, 0, 32);
    goto LAB9;

LAB14:    xsi_set_current_line(29, ng0);

LAB17:    xsi_set_current_line(31, ng0);
    t16 = (t0 + 2408);
    t17 = (t16 + 56U);
    t18 = *((char **)t17);
    t19 = ((char*)((ng4)));
    memset(t8, 0, 8);
    xsi_vlog_signed_add(t8, 32, t18, 32, t19, 32);
    t20 = (t0 + 2408);
    xsi_vlogvar_assign_value(t20, t8, 0, 0, 32);
    xsi_set_current_line(33, ng0);
    t2 = (t0 + 1768);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t0 + 1448);
    t6 = (t5 + 56U);
    t9 = *((char **)t6);
    t15 = (t0 + 1928);
    t16 = (t15 + 56U);
    t17 = *((char **)t16);
    t18 = (t0 + 1608);
    t19 = (t18 + 56U);
    t20 = *((char **)t19);
    t21 = (t0 + 2088);
    t22 = (t21 + 56U);
    t23 = *((char **)t22);
    t24 = (t0 + 1048U);
    t25 = *((char **)t24);
    t24 = (t0 + 2248);
    t26 = (t24 + 56U);
    t27 = *((char **)t26);
    xsi_vlogfile_write(1, 0, 0, ng5, 8, t0, (char)119, t4, 32, (char)118, t9, 32, (char)119, t17, 32, (char)118, t20, 32, (char)119, t23, 32, (char)118, t25, 33, (char)119, t27, 32);
    goto LAB16;

}


extern void work_m_00000000002939334435_1756492367_init()
{
	static char *pe[] = {(void *)Initial_15_0};
	xsi_register_didat("work_m_00000000002939334435_1756492367", "isim/KoggeStone32b_tb_isim_beh.exe.sim/work/m_00000000002939334435_1756492367.didat");
	xsi_register_executes(pe);
}
