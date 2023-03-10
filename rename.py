import os
import chardet  # module to detect file encoding

# Step 01 - Delete files or folder which we can't move

def delete_files(char_to_delete):
    # Delete each file or folder in the current directory if it contains the specified character
    for file in os.listdir('.'):
        if char_to_delete.lower() in file.lower():
            file_path = os.path.join('.', file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("Deleted file:", file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
                print("Deleted folder:", file_path)

# List of character strings to look for in the file or folder name
chars_to_delete = ["y_g4d", "y_sd1", "cus0.xml", "cus1.xml", 
    "tobj", "shi5.xml", "fugr", "chdo.xml", "ZMG_HFX_", "zmg_hfx_",
    ".iwom.xml", ".iwsg.xml", "sicf.xml", "susc.xml", "nrob.xml", "zz_", "CI_",
    "sush.xml", ".iwvb.xml", ".iwmno.xml", ".iwsv.xml", ".iwmo.xml", "avas.xml",
    "wapa.ui5", ".smim.manifest", ".xdp", ".xlsx", "z200zbrc", "z200zbrq", "z200zgen"
    "z200zptc", "-annotation.xml", "component.js", "styles.css", ".controller.js",
    "i18n.properties", "fragment.xml", ".html", ".json", "formatter.js", "model.js", "utility.js",
    "i18n_en.properties", "sfpi.xml", "constants.js", "dialoghelper.js", "wapa.xml", 
    "mockserver.js", "van.xml", "changes_loader.js", "changes_preview.js", "z100zaap0000000",
    "z100zbrc0000000", "z100zbrq0000000", "z100zptc0000000", "z200zaap000000", "z200zgen0000000",
    ".smim.xml", "z200zptc000000", "srvb.xml", "sfpf.xml", "metadata.xml", "wdyn.xml",
    "ZAST_TRM_", "ZZS_TRM", "style.css", "models.js", ".view.xml", 
    "-.library", ".js", "messagebundle.properties", "notes.view.xml", ".less",
     ".ui5repositorytextfiles", ".css", "sprx.xml", "pdts.xml", "z_ossnote", ".htm" ]

# Call the delete_files function for each character string in the list
for char in chars_to_delete:
    delete_files(char)

# Step 02 - Rename files or folders 

def rename_files(old_new_pairs):
    # Rename each file or subfolder in the current directory based on the starting characters
    for file in os.listdir('.'):
        for old_chars, new_chars in old_new_pairs:
            if file.lower().startswith(old_chars.lower()):
                old_path = os.path.join('.', file)
                new_name = file.lower().replace(old_chars.lower(), new_chars)
                new_path = os.path.join('.', new_name)
                os.rename(old_path, new_path)
                print(old_path, "is renamed to", new_path)
                break  # Stop looking for old_chars in the other pairs

# Specify the starting characters and new characters for the folder to look for and replace
old_new_pairs = [
    ('z_trm_', '#GRAV#'),
    ('z_ca_trm_', '#GRAV#CA_'),
    ('zcl_trm_', '#GRAV#CL_'),
    ('zcx_trm_', '#GRAV#CX_'),
    ('zda_trm_', '#GRAV#DA_'),
    ('zst_trm_', '#GRAV#ST_'),
    ('ztt_trm_', '#GRAV#TT_'),
    ('ztrm_', '#GRAV#'),
    ('zbc_', '#GRAV#'),
    ('zds_', '#GRAV#ST_'),
    ('zi_trm_', '#GRAV#I_'),
    ('zp_trm_', '#GRAV#P_'),
    ('zc_trm_', '#GRAV#C_'),
    ('zm_', '#GRAV#M_'),
    ('zvi_trm_', '#GRAV#I_'),
    ('zv_trm_', '#GRAV#V_'),
    ('zcf_trm_', '#GRAV#CF_'),
    ('zdc_trm_', '#GRAV#DC_'),
    ('ze_trm_', '#GRAV#E_'),
    ('zif_trm_', '#GRAV#IF_'),
    ('zsb_trm_', '#GRAV#SB_'),
    ('zsd_trm_', '#GRAV#SD_'),
    ('zapi_trm_', '#GRAV#API_'),
    ('zapi_i_trm_', '#GRAV#API_'),
    ('zbp_i_trm_', '#GRAV#BP_'),
    ('zeml_trm_', '#GRAV#EML_'),
    ('zsms_trm_', '#GRAV#SMS_'),
    ('zui_trm_', '#GRAV#UI_'),
    ('Z_I_TRM_', '#GRAV#I_'),
    ('ZA_TRM_', '#GRAV#A_'),
    ('#GRAV#ST_trm_', '#GRAV#ST_') ,
    ('zdt_trm_', '#GRAV#DT_'),
    ('z_brfp_', '#GRAV#'),
    ('zdv_trm_', '#GRAV#DV_'),
    ('zcl_migfile', '#GRAV#CL_MIGFILE'),
    ('zmig_', '#GRAV#MIG_'),
    ('zde_mig_', '#GRAV#MIG_'),
    ('zmig2', '#GRAV#mig2'),
    ('zdo_mig_', '#GRAV#MIG_'),
    ('zei_badi_', '#GRAV#EI_'),
    ('zsh_trm_', '#GRAV#V_'),
    ('zei_trm_', '#GRAV#E_'),
    ('zct_trm_', '#GRAV#CL_'),
    ('zctl_trm_', '#GRAV#CL_'),
    ('zcl_fica_', '#GRAV#CL_'),
    ('zcl_im_trm_', '#GRAV#CL_'),
    ('zst_', '#GRAV#ST_'), 
    ('ztt_', '#GRAV#TT_'),
    ('zbp_trm_', '#GRAV#CL_'),
    ('zws_trm_', '#GRAV#WS_'),
    ('zvc_trm_', '#GRAV#VC_'),
    ('zca_indpay', '#GRAV#CA_INDPAY'),
    ('zca_cntacc', '#GRAV#CA_CNTACC'),
    ('ZCL_APP_', '#GRAV#CL_APP_'),
    ('zcl_fssc_e2e_sscf4_', '#GRAV#CL_SSCF4_'),
    ('zl_srqm_inc_incidentheade', '#GRAV#CL_SRQM_INCIDENTHEAD'),
    ('zvi_', '#GRAV#V_'),
    ('zvi_trma', '#GRAV#VI_'),
    ('zvi_trmb', '#GRAV#VI_'),
    ('zvi_trmc', '#GRAV#VI_'),
    ('zvi_trmd', '#GRAV#VI_'),
    ('zvi_trme', '#GRAV#VI_'),
    ('zvi_trmf', '#GRAV#VI_'),
    ('zvi_trmg', '#GRAV#VI_'),
    ('zvi_trmh', '#GRAV#VI_'),
    ('zvi_trmi', '#GRAV#VI_'),
    ('zvi_trmj', '#GRAV#VI_'),
    ('zvi_trmk', '#GRAV#VI_'),
    ('zvi_trml', '#GRAV#VI_'),
    ('zvi_trm,', '#GRAV#VI_'),
    ('zvi_trmn', '#GRAV#VI_'),
    ('zvi_trmo', '#GRAV#VI_'),
    ('zvi_trmp', '#GRAV#VI_'),
    ('zvi_trmq', '#GRAV#VI_'),
    ('zvi_trmr', '#GRAV#VI_'),
    ('zvi_trms', '#GRAV#VI_'),
    ('zvi_trmt', '#GRAV#VI_'),
    ('zvi_trmu', '#GRAV#VI_'),
    ('zvi_trmv', '#GRAV#VI_'),
    ('zvi_trmw', '#GRAV#VI_'),
    ('zvi_trmx', '#GRAV#VI_'),
    ('zvi_trmy', '#GRAV#VI_'),
    ('zvi_trmz', '#GRAV#VI_'),
    ('zvp_trma', '#GRAV#VP_'),
    ('zvp_trmb', '#GRAV#VP_'),
    ('zvp_trmc', '#GRAV#VP_'),
    ('zvp_trmd', '#GRAV#VP_'),
    ('zvp_trme', '#GRAV#VP_'),
    ('zvp_trmf', '#GRAV#VP_'),
    ('zvp_trmg', '#GRAV#VP_'),
    ('zvp_trmh', '#GRAV#VP_'),
    ('zvp_trmi', '#GRAV#VP_'),
    ('zvp_trmj', '#GRAV#VP_'),
    ('zvp_trmk', '#GRAV#VP_'),
    ('zvp_trml', '#GRAV#VP_'),
    ('zvp_trm,', '#GRAV#VP_'),
    ('zvp_trmn', '#GRAV#VP_'),
    ('zvp_trmo', '#GRAV#VP_'),
    ('zvp_trmp', '#GRAV#VP_'),
    ('zvp_trmq', '#GRAV#VP_'),
    ('zvp_trmr', '#GRAV#VP_'),
    ('zvp_trms', '#GRAV#VP_'),
    ('zvp_trmt', '#GRAV#VP_'),
    ('zvp_trmu', '#GRAV#VP_'),
    ('zvp_trmv', '#GRAV#VP_'),
    ('zvp_trmw', '#GRAV#VP_'),
    ('zvp_trmx', '#GRAV#VP_'),
    ('zvp_trmy', '#GRAV#VP_'),
    ('zvp_trmz', '#GRAV#VP_'),
    ('zvc_trma', '#GRAV#VC_'),
    ('zvc_trmb', '#GRAV#VC_'),
    ('zvc_trmc', '#GRAV#VC_'),
    ('zvc_trmd', '#GRAV#VC_'),
    ('zvc_trme', '#GRAV#VC_'),
    ('zvc_trmf', '#GRAV#VC_'),
    ('zvc_trmg', '#GRAV#VC_'),
    ('zvc_trmh', '#GRAV#VC_'),
    ('zvc_trmi', '#GRAV#VC_'),
    ('zvc_trmj', '#GRAV#VC_'),
    ('zvc_trmk', '#GRAV#VC_'),
    ('zvc_trml', '#GRAV#VC_'),
    ('zvc_trm,', '#GRAV#VC_'),
    ('zvc_trmn', '#GRAV#VC_'),
    ('zvc_trmo', '#GRAV#VC_'),
    ('zvc_trmp', '#GRAV#VC_'),
    ('zvc_trmq', '#GRAV#VC_'),
    ('zvc_trmr', '#GRAV#VC_'),
    ('zvc_trms', '#GRAV#VC_'),
    ('zvc_trmt', '#GRAV#VC_'),
    ('zvc_trmu', '#GRAV#VC_'),
    ('zvc_trmv', '#GRAV#VC_'),
    ('zvc_trmw', '#GRAV#VC_'),
    ('zvc_trmx', '#GRAV#VC_'),
    ('zvc_trmy', '#GRAV#VC_'),
    ('zvc_trmz', '#GRAV#VC_')
]

# Call the rename_files function with the old_new_pairs array
rename_files(old_new_pairs)

# Step 03 - Change all occurrences of string in the files

replacements = [        
('Z_TRM_', '/GRAV/'),
('z_trm_', '/GRAV/'),

('ZCL_TRM_', '/GRAV/CL_'),
('zcl_trm_', '/GRAV/CL_'),
         
('ZDC_TRM_', '/GRAV/DC_'),
('zdc_trm_', '/GRAV/DC_'),

('ZC_TRM_', '/GRAV/C_'),
('zc_trm_', '/GRAV/C_'),

('ZI_TRM_', '/GRAV/I_'),
('zi_trm_', '/GRAV/I_'),

('ZP_TRM_', '/GRAV/P_'),
('zp_trm_', '/GRAV/P_'),

('ZCX_TRM_', '/GRAV/CX_'),
('zcx_trm_', '/GRAV/CX_'),
         
('ZST_TRM_', '/GRAV/ST_'),
('zst_trm_', '/GRAV/ST_'),

('Z_CA_TRM_', '/GRAV/CA_'),
('z_ca_trm_', '/GRAV/CA_'),
	 
('ZDS_', '/GRAV/ST_'),
('zds_', '/GRAV/ST_'),

('ZVI_TRM_', '/GRAV/VI_'),
('zvi_trm_', '/GRAV/VI_'),

('ZTT_TRM_', '/GRAV/TT_'),
('ztt_trm_', '/GRAV/TT_'),

('ZV_TRM_', '/GRAV/V_'),
('zv_trm_', '/GRAV/V_'),

('ZCF_TRM_', '/GRAV/CF_'),
('zcf_trm_', '/GRAV/CF_'),

('ZIF_TRM_', '/GRAV/IF_'),
('zif_trm_', '/GRAV/IF_'),
  
('ZDA_TRM_', '/GRAV/DA_'),
('zda_trm_', '/GRAV/DA_'),

('ZVC_TRM_', '/GRAV/VC_'),
('zvc_trm_', '/GRAV/VC_'),

('ZSB_TRM_', '/GRAV/SB_'),
('zsb_trm_', '/GRAV/SB_'),

('ZDT_TRM_', '/GRAV/DT_'),
('zdt_trm_', '/GRAV/DT_'),
   
('ZSD_TRM_', '/GRAV/SD_'), 
('zsd_trm_', '/GRAV/SD_'),

('ZE_TRM_', '/GRAV/E_'), 
('ze_trm_', '/GRAV/E_'),
  
('ZVE_TRM_', '/GRAV/VE_'),
('zve_trm_', '/GRAV/VE_'),

('ZI(C)_T', '/GRAV/I(C)'),

('ZBP_I_TRM_', '/GRAV/BP_'),
('zbp_i_trm_', '/GRAV/BP_'),
   
('ZAPI_TRM_', '/GRAV/API_'), 
('zapi_trm_', '/GRAV/API_'),

('ZEML_TRM_', '/GRAV/EML_'), 
('zeml_trm_', '/GRAV/EML_'),

('ZSMS_TRM_', '/GRAV/SMS_'), 
('zsms_trm_', '/GRAV/SMS_'),

('ZUI_TRM_', '/GRAV/UI_'), 
('zui_trm_', '/GRAV/UI_'),

('Z_I_TRM_', '/GRAV/I_'),
('z_i_trm_', '/GRAV/I_'),

('ZA_TRM_', '/GRAV/A_'),
('za_trm_', '/GRAV/A_'),

('ZVP_TRM_', '/GRAV/VP_'),
('zvp_trm_', '/GRAV/VP_'),

('ZPI_TRM_', '/GRAV/VP_'),
('zpi_trm_', '/GRAV/VP_'),

('/GRAV/ST_TRM_', '/GRAV/ST_'),
('/grav/st_trm_', '/GRAV/ST_'),

('ZCA_TRM_', '/GRAV/CA_'),
('zca_trm_', '/GRAV/CA_'),

('ZVH_TRM_', '/GRAV/I_H'),
('zvh_trm_', '/GRAV/I_H'),

('Zc_TRM_', '/GRAV/C_'),

('Z_BRFP_', '/GRAV/'),
('z_brfp_', '/GRAV/'),

('ZDV_TRM_', '/GRAV/DV_'),
('zdv_trm_', '/GRAV/DV_'),

('ZCL_MIGFILE', '/GRAV/CL_MIGFILE'),
('zcl_migfile', '/GRAV/CL_MIGFILE'),

('ZMIG_', '/GRAV/MIG_'),
('zmig_', '/GRAV/MIG_'),

('ZDE_MIG_', '/GRAV/MIG_'),
('zde_mig_', '/GRAV/MIG_'),

('ZMIG2', '/GRAV/MIG2'),
('zmig2', '/GRAV/MIG2'),

('ZDO_MIG_', '/GRAV/MIG_'),
('zdo_mig_', '/GRAV/MIG_'),

('ZCP_TRM_', '/GRAV/P_'),
('Zcp_TRM_', '/GRAV/P_'),

('ZEI_BADI_', '/GRAV/EI_'),
('zei_badi_', '/GRAV/EI_'),

('zsh_trm_', '/GRAV/V_'),
('ZSH_TRM_', '/GRAV/V_'),

('ZEI_TRM_', '/GRAV/E_'),
('zei_trm_', '/GRAV/E_'),

('ZCT_TRM_', '/GRAV/CL_'),
('zct_trm_', '/GRAV/CL_'),

('ZCTL_TRM_', '/GRAV/CL_'),
('zctl_trm_', '/GRAV/CL_'),

('zcl_fica_', '/GRAV/CL_'),
('ZCL_FICA_', '/GRAV/CL_'),

('ZCL_IM_TRM_', '/GRAV/CL_'),
('zcl_im_trm_', '/GRAV/CL_'),
    
('Zi_TRM_', '/GRAV/I_'),

('ZST_', '/GRAV/ST_'),
('zst_', '/GRAV/ST_'), 

('ZTT_', '/GRAV/TT_'),
('ztt_', '/GRAV/TT_'),

('ZVT_TRM_', '/GRAV/I_'),

('ZBP_TRM_', '/GRAV/CL_'), 
('zbp_trm_', '/GRAV/CL_'),

('ZWS_TRM_', '/GRAV/WS_'),
('zws_trm_', '/GRAV/WS_'),

('ZCA_CNTACC', '/GRAV/CA_CNTACC'),
('zca_cntacc', '/GRAV/CA_CNTACC'),

('ZCA_INDPAY', '/GRAV/CA_INDPAY'),
('zca_indpay', '/GRAV/CA_INDPAY'),

('ZCL_APP_', '/GRAV/CL_APP_'),
('zcl_app_', '/GRAV/CL_APP_'),

('ZCL_FDDC_E2E_SSCF4_', '/GRAV/CL_SSCF4_'),
('zcl_fddc_e2e_sscf4_', '/GRAV/CL_SSCF4_'),

('ZL_SRQM_INC_INCIDENTHEADE', '/GRAV/CL_SRQM_INCIDENTHEAD'),
('zl_srqm_inc_incidentheade', '/GRAV/CL_SRQM_INCIDENTHEAD'),

('ZVI_A', '/GRAV/VI_'),
('ZVI_B', '/GRAV/VI_'),
('ZVI_C', '/GRAV/VI_'),
('ZVI_D', '/GRAV/VI_'),
('ZVI_E', '/GRAV/VI_'),
('ZVI_F', '/GRAV/VI_'),
('ZVI_G', '/GRAV/VI_'),
('ZVI_H', '/GRAV/VI_'),
('ZVI_I', '/GRAV/VI_'),
('ZVI_G', '/GRAV/VI_'),
('ZVI_H', '/GRAV/VI_'),
('ZVI_I', '/GRAV/VI_'),
('ZVI_J', '/GRAV/VI_'),
('ZVI_K', '/GRAV/VI_'),
('ZVI_L', '/GRAV/VI_'),
('ZVI_M', '/GRAV/VI_'),
('ZVI_N', '/GRAV/VI_'),
('ZVI_O', '/GRAV/VI_'),
('ZVI_P', '/GRAV/VI_'),
('ZVI_Q', '/GRAV/VI_'),
('ZVI_R', '/GRAV/VI_'),
('ZVI_S', '/GRAV/VI_'),
('ZVI_T', '/GRAV/VI_'),
('ZVI_U', '/GRAV/VI_'),
('ZVI_V', '/GRAV/VI_'),
('ZVI_W', '/GRAV/VI_'),
('ZVI_X', '/GRAV/VI_'),
('ZVI_Y', '/GRAV/VI_'),
('ZVI_Z', '/GRAV/VI_'),

('ZVI_TRMA', '/GRAV/VI_'),
('ZVI_TRMB', '/GRAV/VI_'),
('ZVI_TRMC', '/GRAV/VI_'),
('ZVI_TRMD', '/GRAV/VI_'),
('ZVI_TRME', '/GRAV/VI_'),
('ZVI_TRMF', '/GRAV/VI_'),
('ZVI_TRMG', '/GRAV/VI_'),
('ZVI_TRMI', '/GRAV/VI_'),
('ZVI_TRMJ', '/GRAV/VI_'),
('ZVI_TRMK', '/GRAV/VI_'),
('ZVI_TRML', '/GRAV/VI_'),
('ZVI_TRMM', '/GRAV/VI_'),
('ZVI_TRMN', '/GRAV/VI_'),
('ZVI_TRMO', '/GRAV/VI_'),
('ZVI_TRMP', '/GRAV/VI_'),
('ZVI_TRMQ', '/GRAV/VI_'),
('ZVI_TRMR', '/GRAV/VI_'),
('ZVI_TRMS', '/GRAV/VI_'),
('ZVI_TRMT', '/GRAV/VI_'),
('ZVI_TRMU', '/GRAV/VI_'),
('ZVI_TRMV', '/GRAV/VI_'),
('ZVI_TRMW', '/GRAV/VI_'),
('ZVI_TRMX', '/GRAV/VI_'),
('ZVI_TRMY', '/GRAV/VI_'),
('ZVI_TRMZ', '/GRAV/VI_'),

('ZVP_TRMA', '/GRAV/VP_'),
('ZVP_TRMB', '/GRAV/VP_'),
('ZVP_TRMC', '/GRAV/VP_'),
('ZVP_TRMD', '/GRAV/VP_'),
('ZVP_TRME', '/GRAV/VP_'),
('ZVP_TRMF', '/GRAV/VP_'),
('ZVP_TRMG', '/GRAV/VP_'),
('ZVP_TRMF', '/GRAV/VP_'),
('ZVP_TRMI', '/GRAV/VP_'),
('ZVP_TRMJ', '/GRAV/VP_'),
('ZVP_TRMK', '/GRAV/VP_'),
('ZVP_TRML', '/GRAV/VP_'),
('ZVP_TRMM', '/GRAV/VP_'),
('ZVP_TRMN', '/GRAV/VP_'),
('ZVP_TRMO', '/GRAV/VP_'),
('ZVP_TRMP', '/GRAV/VP_'),
('ZVP_TRMQ', '/GRAV/VP_'),
('ZVP_TRMR', '/GRAV/VP_'),
('ZVP_TRMS', '/GRAV/VP_'),
('ZVP_TRMT', '/GRAV/VP_'),
('ZVP_TRMU', '/GRAV/VP_'),
('ZVP_TRMW', '/GRAV/VP_'),
('ZVP_TRMX', '/GRAV/VP_'),
('ZVP_TRMY', '/GRAV/VP_'),
('ZVP_TRMZ', '/GRAV/VP_'),

('ZVC_TRMA', '/GRAV/VP_C'),
('ZVC_TRMB', '/GRAV/VP_C'),
('ZVC_TRMC', '/GRAV/VP_C'),
('ZVC_TRMD', '/GRAV/VP_C'),
('ZVC_TRME', '/GRAV/VP_C'),
('ZVC_TRMF', '/GRAV/VP_C'),
('ZVC_TRMG', '/GRAV/VP_C'),
('ZVC_TRMH', '/GRAV/VP_C'),
('ZVC_TRMI', '/GRAV/VP_C'),
('ZVC_TRMJ', '/GRAV/VP_C'),
('ZVC_TRMK', '/GRAV/VP_C'),
('ZVC_TRML', '/GRAV/VP_C'),
('ZVC_TRMM', '/GRAV/VP_C'),
('ZVC_TRMN', '/GRAV/VP_C'),
('ZVC_TRMO', '/GRAV/VP_C'),
('ZVC_TRMP', '/GRAV/VP_C'),
('ZVC_TRMQ', '/GRAV/VP_C'),
('ZVC_TRMR', '/GRAV/VP_C'),
('ZVC_TRMS', '/GRAV/VP_C'),
('ZVC_TRMT', '/GRAV/VP_C'),
('ZVC_TRMU', '/GRAV/VP_C'),
('ZVC_TRMV', '/GRAV/VP_C'),
('ZVC_TRMW', '/GRAV/VP_C'),
('ZVC_TRMX', '/GRAV/VP_C'),
('ZVC_TRMY', '/GRAV/VP_C'),
('ZVC_TRMZ', '/GRAV/VP_C')  
]

# Loop over all files in the current directory and its subdirectories
for root, dirs, files in os.walk('.'):
    for file_name in files:
        if file_name != 'rename.py':
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'rb') as f:
                    # Use chardet to detect the file encoding
                    result = chardet.detect(f.read())
                    encoding = result['encoding']
                    # Open the file with the detected encoding and read the contents
                    with open(file_path, 'r', encoding=encoding) as f:
                        file_contents = f.read()
            except (UnicodeDecodeError, FileNotFoundError):
                continue  # Skip the file if it cannot be opened or decoded

            # Loop over all replacements and replace all occurrences of the string with the replacement string
            for string_to_replace, replacement_string in replacements:
                # Replace all occurrences of the string with the replacement string, ignoring case
                file_contents = file_contents.replace(string_to_replace, replacement_string, -1)

            # Write the modified contents back to the file
            with open(file_path, 'w', encoding=encoding) as f:
                f.write(file_contents)
            print("Text replaced in file", file_path)