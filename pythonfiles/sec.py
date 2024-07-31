# a= ["family_id",	"member_id",	"unique_health_id"	,"phr_family_id",	"makkal_number"	,
#     "ndhm_id",	"member_name",	"member_local_name",	"relationshipwith",	"relationship",	
#     "birth_date",	"gender",	"mobile_number",	"alt_mobile_number",	"email",	"alt_email",	
#     "aadhaar_number",	"voter_id",	"welfare_beneficiary_ids",	"program_ids",	"eligible_couple_id	",
#     "country_id	","state_id",	"district_id",	"hud_id",	"block_id",	"taluk_id",	"village_id",	
#     "rev_village_id",	"habitation_id",	"ward_id","area_id","street_id",	"facility_id",	"resident_status",	
#     "resident_status_details",	"update_register",	",last_update_date",	"consent_status",	
#     "consent_details",	"hims_id",	"abha_id",	"abha_address",	"immunization_status",	"premature_baby",	
#     "congenital_defects",	"blood_group",	"attended_age",	"ifa_tablet_provided",	"sanitary_napkin_provided",	
#     "anemia_yes_or_no",	"pregnant_yes_or_no",	"antenatal_postnatal",	"prolonged_disease",	
#     "non_communicable_disease",	"communicable_disease",	"consanguineous_marriage",	"rch_id",	
#     "is_verified",	"insurances	address",	"mtm_id"
# ]



# b=[
#     "family_id",	"phr_family_id",	"family_head",	"family_members_count",	"pds_smart_card_id",	
#     "pds_old_card_id",	"family_insurances",	"shop_id",	"country_id",	"state_id",	"district_id",	"hud_id",	
#     "block_id",	"taluk_id",	"village_id",	"rev_village_id",	"habitation_id",	"area_id",	"ward_id",	"street_id",	
#     "pincode",	"door_no",	"apartment_name",	"postal_address",	"facility_id",	"latitude",	"longitude",	
#     "update_register",	"last_update_date",	"hhg_id",	"hsc_unit_id",	"reside_status"
#     ]


# c=[]

# for i in b:
#     if i not in a:
#         c.append (i)
# print(c)        



# a=[
#     'district_id',	'family_count',	'family_member_count',	'screening_count',	'male_count',
#     'female_count',	'transgender_count',	'member_18_45_count',	'member_45_above',	
#     'verified_mem_count',	'mem_married_male',	'mem_married_female',	'mem_0_1',	'mem_2_5',
#     'mem_6_12',	'mtm_count',	'drug_issued_count',	'mem_46_59',	'mem_60_above',
#     'mem_below_3',	'mem_3_6',	'mem_7_9',	'mem_10_19',	'resident_count',	'death_count',
#     'migrants_count',	'non_traceables_count',	'dublicate_count',	'member_added',	'family_added',
#     'urban_scr',	'rural_scr',	'municipalty_scr',	'corporation_scr',	'uhc_total_op',	'uhc_male_op',
#     'uhc_female_op',	'uhc_referral',	'uhc_op_facility_daya',	'uhc_labtest_day',	'uhc_drug_day'

# ]

# b=[
        
#     "family_id",	"phr_family_id",	"family_head",	"family_members_count",	"pds_smart_card_id",	
#     "pds_old_card_id",	"family_insurances",	"shop_id",	"country_id",	"state_id",	"district_id",	"hud_id",	
#     "block_id",	"taluk_id",	"village_id",	"rev_village_id",	"habitation_id",	"area_id",	"ward_id",	"street_id",	
#     "pincode",	"door_no",	"apartment_name",	"postal_address",	"facility_id",	"latitude",	"longitude",	
#     "update_register",	"last_update_date",	"hhg_id",	"hsc_unit_id",	"reside_status"

#     ]


# c=["family_id",	"member_id",	"unique_health_id"	,"phr_family_id",	"makkal_number"	,
#     "ndhm_id",	"member_name",	"member_local_name",	"relationshipwith",	"relationship",	
#     "birth_date",	"gender",	"mobile_number",	"alt_mobile_number",	"email",	"alt_email",	
#     "aadhaar_number",	"voter_id",	"welfare_beneficiary_ids",	"program_ids",	"eligible_couple_id	",
#     "country_id	","state_id",	"district_id",	"hud_id",	"block_id",	"taluk_id",	"village_id",	
#     "rev_village_id",	"habitation_id",	"ward_id","area_id","street_id",	"facility_id",	"resident_status",	
#     "resident_status_details",	"update_register",	",last_update_date",	"consent_status",	
#     "consent_details",	"hims_id",	"abha_id",	"abha_address",	"immunization_status",	"premature_baby",	
#     "congenital_defects",	"blood_group",	"attended_age",	"ifa_tablet_provided",	"sanitary_napkin_provided",	
#     "anemia_yes_or_no",	"pregnant_yes_or_no",	"antenatal_postnatal",	"prolonged_disease",	
#     "non_communicable_disease",	"communicable_disease",	"consanguineous_marriage",	"rch_id",	
#     "is_verified",	"insurances	address",	"mtm_id"
# ]
# print(len(c))





a = ['family_id', 'phr_family_id', 'family_head', 'family_members_count', 'pds_smart_card_id', 'pds_old_card_id', 'family_insurances', 'shop_id', 'country_id', 'state_id', 'district_id', 'hud_id', 'block_id', 'taluk_id', 'village_id', 'rev_village_id', 'habitation_id', 'area_id', 'ward_id', 'street_id', 'pincode', 'door_no', 'apartment_name', 'postal_address', 'facility_id', 'latitude', 'longitude', 'update_register', 'last_update_date', 'hhg_id', 'hsc_unit_id', 'reside_status']

b = ['family_id', 'member_id', 'unique_health_id', 'phr_family_id', 'makkal_number', 'ndhm_id', 'member_name', 'member_local_name', 'relationshipwith', 'relationship', 'birth_date', 'gender', 'mobile_number', 'alt_mobile_number', 'email', 'alt_email', 'aadhaar_number', 'voter_id', 'insurances', 'welfare_beneficiary_ids', 'program_ids', 'eligible_couple_id', 'country_id', 'state_id', 'district_id', 'hud_id', 'block_id', 'taluk_id', 'village_id', 'rev_village_id', 'habitation_id', 'ward_id', 'area_id', 'street_id', 'facility_id', 'resident_status', 'resident_status_details', 'update_register', 'last_update_date', 'consent_status', 'consent_details', 'hmis_id', 'biometric_data', 'abha_id', 'hims_id', 'auth_token', 'abha_address', 'attended_age', 'non_communicable_disease', 'communicable_disease', 'immunization_status', 'premature_baby', 'congenital_defects', 'blood_group', 'ifa_tablet_provided', 'sanitary_napkin_provided', 'anemia_yes_or_no', 'pregnant_yes_or_no', 'antenatal_postnatal', 'prolonged_disease', 'consanguineous_marriage', 'rch_id', 'is_verified']

c = []

for i in a:
    if i not in b:
        c.append(i)

print(c)




