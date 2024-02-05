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
static const char *ng0 = "C:/Users/Dr.Fly/Desktop/FPGAAdders/BrentKung16b_tb.v";
static int ng1[] = {1, 0};
static int ng2[] = {0, 0};
static const char *ng3 = "Missmatch : %dD(%bB) + %dD(%bB) => %dD(%bB) != %dD";
static const char *ng4 = "OK : %dD(%bB) + %dD(%bB) => %dD(%bB) != %dD";
static const char *ng5 = "Total Error count is %d";



static void Initial_17_0(char *t0)
{
    char t13[8];
    char t19[8];
    char *t1;
    char *t2;
    char *t3;
    char *t4;
    char *t5;
    unsigned int t6;
    unsigned int t7;
    unsigned int t8;
    unsigned int t9;
    unsigned int t10;
    char *t11;
    char *t12;
    char *t14;
    char *t15;
    char *t16;
    char *t17;
    char *t18;
    char *t20;
    char *t21;
    char *t22;
    char *t23;
    char *t24;
    char *t25;
    char *t26;
    char *t27;
    char *t28;
    unsigned int t29;
    unsigned int t30;
    unsigned int t31;
    unsigned int t32;
    unsigned int t33;
    unsigned int t34;
    unsigned int t35;
    unsigned int t36;
    unsigned int t37;
    unsigned int t38;
    unsigned int t39;
    unsigned int t40;

LAB0:    t1 = (t0 + 3168U);
    t2 = *((char **)t1);
    if (t2 == 0)
        goto LAB2;

LAB3:    goto *t2;

LAB2:    xsi_set_current_line(17, ng0);

LAB4:    xsi_set_current_line(19, ng0);
    t2 = ((char*)((ng1)));
    t3 = (t0 + 1928);
    xsi_vlogvar_assign_value(t3, t2, 0, 0, 1);
    xsi_set_current_line(21, ng0);
    t2 = ((char*)((ng1)));
    t3 = (t0 + 2088);
    xsi_vlogvar_assign_value(t3, t2, 0, 0, 1);
    xsi_set_current_line(23, ng0);
    t2 = ((char*)((ng2)));
    t3 = (t0 + 1448);
    xsi_vlogvar_assign_value(t3, t2, 0, 0, 16);
    xsi_set_current_line(25, ng0);
    t2 = ((char*)((ng2)));
    t3 = (t0 + 1608);
    xsi_vlogvar_assign_value(t3, t2, 0, 0, 16);
    xsi_set_current_line(27, ng0);

LAB5:    t2 = (t0 + 1928);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t4 + 4);
    t6 = *((unsigned int *)t5);
    t7 = (~(t6));
    t8 = *((unsigned int *)t4);
    t9 = (t8 & t7);
    t10 = (t9 != 0);
    if (t10 > 0)
        goto LAB6;

LAB7:    xsi_set_current_line(69, ng0);
    t2 = (t0 + 2248);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    xsi_vlogfile_write(1, 0, 0, ng5, 2, t0, (char)119, t4, 32);

LAB1:    return;
LAB6:    xsi_set_current_line(27, ng0);

LAB8:    xsi_set_current_line(29, ng0);
    t11 = ((char*)((ng1)));
    t12 = (t0 + 2088);
    xsi_vlogvar_assign_value(t12, t11, 0, 0, 1);
    xsi_set_current_line(31, ng0);

LAB9:    t2 = (t0 + 2088);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t4 + 4);
    t6 = *((unsigned int *)t5);
    t7 = (~(t6));
    t8 = *((unsigned int *)t4);
    t9 = (t8 & t7);
    t10 = (t9 != 0);
    if (t10 > 0)
        goto LAB10;

LAB11:    xsi_set_current_line(57, ng0);
    t2 = (t0 + 1448);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng1)));
    memset(t13, 0, 8);
    xsi_vlog_unsigned_add(t13, 32, t4, 16, t5, 32);
    t11 = (t0 + 1448);
    xsi_vlogvar_assign_value(t11, t13, 0, 0, 16);
    xsi_set_current_line(59, ng0);
    t2 = (t0 + 1448);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng2)));
    memset(t13, 0, 8);
    t11 = (t4 + 4);
    t12 = (t5 + 4);
    t6 = *((unsigned int *)t4);
    t7 = *((unsigned int *)t5);
    t8 = (t6 ^ t7);
    t9 = *((unsigned int *)t11);
    t10 = *((unsigned int *)t12);
    t29 = (t9 ^ t10);
    t30 = (t8 | t29);
    t31 = *((unsigned int *)t11);
    t32 = *((unsigned int *)t12);
    t33 = (t31 | t32);
    t34 = (~(t33));
    t35 = (t30 & t34);
    if (t35 != 0)
        goto LAB32;

LAB29:    if (t33 != 0)
        goto LAB31;

LAB30:    *((unsigned int *)t13) = 1;

LAB32:    t15 = (t13 + 4);
    t36 = *((unsigned int *)t15);
    t37 = (~(t36));
    t38 = *((unsigned int *)t13);
    t39 = (t38 & t37);
    t40 = (t39 != 0);
    if (t40 > 0)
        goto LAB33;

LAB34:
LAB35:    goto LAB5;

LAB10:    xsi_set_current_line(31, ng0);

LAB12:    xsi_set_current_line(33, ng0);
    t11 = (t0 + 2976);
    xsi_process_wait(t11, 1000LL);
    *((char **)t1) = &&LAB13;
    goto LAB1;

LAB13:    xsi_set_current_line(35, ng0);
    t2 = (t0 + 1048U);
    t3 = *((char **)t2);
    t2 = (t0 + 1768);
    t4 = (t2 + 56U);
    t5 = *((char **)t4);
    memset(t13, 0, 8);
    if (*((unsigned int *)t3) != *((unsigned int *)t5))
        goto LAB15;

LAB14:    t11 = (t3 + 4);
    t12 = (t5 + 4);
    if (*((unsigned int *)t11) != *((unsigned int *)t12))
        goto LAB15;

LAB16:    t14 = (t13 + 4);
    t6 = *((unsigned int *)t14);
    t7 = (~(t6));
    t8 = *((unsigned int *)t13);
    t9 = (t8 & t7);
    t10 = (t9 != 0);
    if (t10 > 0)
        goto LAB17;

LAB18:    xsi_set_current_line(45, ng0);
    t2 = (t0 + 1448);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t0 + 1448);
    t11 = (t5 + 56U);
    t12 = *((char **)t11);
    t14 = (t0 + 1608);
    t15 = (t14 + 56U);
    t16 = *((char **)t15);
    t17 = (t0 + 1608);
    t18 = (t17 + 56U);
    t20 = *((char **)t18);
    t21 = (t0 + 1048U);
    t22 = *((char **)t21);
    t21 = (t0 + 1048U);
    t23 = *((char **)t21);
    t21 = (t0 + 1768);
    t24 = (t21 + 56U);
    t25 = *((char **)t24);
    t26 = (t0 + 1768);
    t27 = (t26 + 56U);
    t28 = *((char **)t27);
    xsi_vlogfile_write(1, 0, 0, ng4, 9, t0, (char)118, t4, 16, (char)118, t12, 16, (char)118, t16, 16, (char)118, t20, 16, (char)118, t22, 17, (char)118, t23, 17, (char)118, t25, 17, (char)118, t28, 17);

LAB19:    xsi_set_current_line(47, ng0);
    t2 = (t0 + 1608);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng1)));
    memset(t13, 0, 8);
    xsi_vlog_unsigned_add(t13, 32, t4, 16, t5, 32);
    t11 = (t0 + 1608);
    xsi_vlogvar_assign_value(t11, t13, 0, 0, 16);
    xsi_set_current_line(49, ng0);
    t2 = (t0 + 1608);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = ((char*)((ng2)));
    memset(t13, 0, 8);
    t11 = (t4 + 4);
    t12 = (t5 + 4);
    t6 = *((unsigned int *)t4);
    t7 = *((unsigned int *)t5);
    t8 = (t6 ^ t7);
    t9 = *((unsigned int *)t11);
    t10 = *((unsigned int *)t12);
    t29 = (t9 ^ t10);
    t30 = (t8 | t29);
    t31 = *((unsigned int *)t11);
    t32 = *((unsigned int *)t12);
    t33 = (t31 | t32);
    t34 = (~(t33));
    t35 = (t30 & t34);
    if (t35 != 0)
        goto LAB24;

LAB21:    if (t33 != 0)
        goto LAB23;

LAB22:    *((unsigned int *)t13) = 1;

LAB24:    t15 = (t13 + 4);
    t36 = *((unsigned int *)t15);
    t37 = (~(t36));
    t38 = *((unsigned int *)t13);
    t39 = (t38 & t37);
    t40 = (t39 != 0);
    if (t40 > 0)
        goto LAB25;

LAB26:
LAB27:    goto LAB9;

LAB15:    *((unsigned int *)t13) = 1;
    goto LAB16;

LAB17:    xsi_set_current_line(35, ng0);

LAB20:    xsi_set_current_line(37, ng0);
    t15 = (t0 + 2248);
    t16 = (t15 + 56U);
    t17 = *((char **)t16);
    t18 = ((char*)((ng1)));
    memset(t19, 0, 8);
    xsi_vlog_signed_add(t19, 32, t17, 32, t18, 32);
    t20 = (t0 + 2248);
    xsi_vlogvar_assign_value(t20, t19, 0, 0, 32);
    xsi_set_current_line(39, ng0);
    t2 = (t0 + 1448);
    t3 = (t2 + 56U);
    t4 = *((char **)t3);
    t5 = (t0 + 1448);
    t11 = (t5 + 56U);
    t12 = *((char **)t11);
    t14 = (t0 + 1608);
    t15 = (t14 + 56U);
    t16 = *((char **)t15);
    t17 = (t0 + 1608);
    t18 = (t17 + 56U);
    t20 = *((char **)t18);
    t21 = (t0 + 1048U);
    t22 = *((char **)t21);
    t21 = (t0 + 1048U);
    t23 = *((char **)t21);
    t21 = (t0 + 1768);
    t24 = (t21 + 56U);
    t25 = *((char **)t24);
    t26 = (t0 + 1768);
    t27 = (t26 + 56U);
    t28 = *((char **)t27);
    xsi_vlogfile_write(1, 0, 0, ng3, 9, t0, (char)118, t4, 16, (char)118, t12, 16, (char)118, t16, 16, (char)118, t20, 16, (char)118, t22, 17, (char)118, t23, 17, (char)118, t25, 17, (char)118, t28, 17);
    goto LAB19;

LAB23:    t14 = (t13 + 4);
    *((unsigned int *)t13) = 1;
    *((unsigned int *)t14) = 1;
    goto LAB24;

LAB25:    xsi_set_current_line(49, ng0);

LAB28:    xsi_set_current_line(51, ng0);
    t16 = ((char*)((ng2)));
    t17 = (t0 + 2088);
    xsi_vlogvar_assign_value(t17, t16, 0, 0, 1);
    goto LAB27;

LAB31:    t14 = (t13 + 4);
    *((unsigned int *)t13) = 1;
    *((unsigned int *)t14) = 1;
    goto LAB32;

LAB33:    xsi_set_current_line(59, ng0);

LAB36:    xsi_set_current_line(61, ng0);
    t16 = ((char*)((ng2)));
    t17 = (t0 + 1928);
    xsi_vlogvar_assign_value(t17, t16, 0, 0, 1);
    goto LAB35;

}


extern void work_m_00000000001929383721_0164184113_init()
{
	static char *pe[] = {(void *)Initial_17_0};
	xsi_register_didat("work_m_00000000001929383721_0164184113", "isim/BrentKung16b_tb_isim_beh.exe.sim/work/m_00000000001929383721_0164184113.didat");
	xsi_register_executes(pe);
}
