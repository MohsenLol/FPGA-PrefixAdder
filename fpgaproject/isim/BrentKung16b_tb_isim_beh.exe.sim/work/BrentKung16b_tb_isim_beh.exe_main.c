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

#include "xsi.h"

struct XSI_INFO xsi_info;



int main(int argc, char **argv)
{
    xsi_init_design(argc, argv);
    xsi_register_info(&xsi_info);

    xsi_register_min_prec_unit(-12);
    work_m_00000000001819883501_3694240535_init();
    work_m_00000000002266876014_3068584386_init();
    work_m_00000000000882865015_4140939458_init();
    work_m_00000000000371521475_1718624373_init();
    work_m_00000000001929383721_0164184113_init();
    work_m_00000000004134447467_2073120511_init();


    xsi_register_tops("work_m_00000000001929383721_0164184113");
    xsi_register_tops("work_m_00000000004134447467_2073120511");


    return xsi_run_simulation(argc, argv);

}
