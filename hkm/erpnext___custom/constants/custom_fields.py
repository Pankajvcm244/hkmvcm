CUSTOM_FIELDS = {
  "Journal Entry": [
    {
      "dt": "Journal Entry",
      "fieldtype": "Data",
      "label": "Bank Statement Name",
      "fieldname": "bank_statement_name",
      "insert_after": "donation_receipt",
      "read_only": 1,
      "hidden": 1,
      "translatable": 1
    }
    # {
    #   "dt": "Journal Entry",
    #   "fieldtype": "Link",
    #   "label": "Donation Receipt",
    #   "fieldname": "donation_receipt",
    #   "insert_after": "tax_withholding_category",
    #   "options": "Donation Receipt"
    # }
  ],
  "Purchase Invoice": [
    {
      "dt": "Purchase Invoice",
      "fieldtype": "Link",
      "label": "Default Difference Account",
      "fieldname": "default_difference_account",
      "insert_after": "sec_warehouse",
      "options": "Account"
    },
    {
      "dt": "Purchase Invoice",
      "fieldtype": "Link",
      "label": "Department",
      "fieldname": "department",
      "insert_after": "amended_from",
      "options": "Department",
      "read_only": 1,
      "in_standard_filter": 1
    }
  ],
  "Material Request Item": [
    {
      "dt": "Material Request Item",
      "fieldtype": "Data",
      "label": "Item Type",
      "fieldname": "item_type",
      "insert_after": "item_name",
      "read_only": 1,
      "in_list_view": 1,
      "translatable": 1
    },
    {
      "dt": "Material Request Item",
      "fieldtype": "Data",
      "label": "Item Description",
      "fieldname": "item_description",
      "insert_after": "section_break_4",
      "Length": 256,
      "translatable": 1
    }
  ],
  "Purchase Order Item": {
    "dt": "Purchase Order Item",
    "fieldtype": "Data",
    "label": "Item Type",
    "fieldname": "item_type",
    "insert_after": "item_name",
    "read_only": 1,
    "in_list_view": 1,
    "translatable": 1
  },
  "Item Tax Template": {
    "dt": "Item Tax Template",
    "fieldtype": "Int",
    "label": "Cumulative Tax",
    "fieldname": "cumulative_tax",
    "insert_after": "disabled"
  },
  "Item": [
    {
      "dt": "Item",
      "fieldtype": "Link",
      "label": "Item Creation Request",
      "fieldname": "item_creation_request",
      "insert_after": "total_projected_qty",
      "options": "Item Creation Request",
      "read_only": 1
    },
    {
      "dt": "Item",
      "fieldtype": "Data",
      "label": "Selling Rate with GST",
      "fieldname": "selling_rate_with_gst",
      "insert_after": "standard_rate",
      "read_only": 1,
      "translatable": 1
    }
  ],
  "Item Creation Request": {
    "dt": "Item Creation Request",
    "fieldtype": "Link",
    "label": "Workflow State",
    "fieldname": "workflow_state",
    "options": "Workflow State",
    "hidden": 1,
    "no_copy": 1,
    "allow_on_submit": 1
  },
  "Supplier Creation Request": {
    "dt": "Supplier Creation Request",
    "fieldtype": "Link",
    "label": "Workflow State",
    "fieldname": "workflow_state",
    "options": "Workflow State",
    "hidden": 1,
    "no_copy": 1,
    "allow_on_submit": 1
  },
  # "Donation Receipt": {
  #   "dt": "Donation Receipt",
  #   "fieldtype": "Link",
  #   "label": "Workflow State",
  #   "fieldname": "workflow_state",
  #   "options": "Workflow State",
  #   "hidden": 1,
  #   "no_copy": 1,
  #   "allow_on_submit": 1
  # },
  "Task": [
    {
      "dt": "Task",
      "fieldtype": "Data",
      "label": "Location",
      "fieldname": "location",
      "insert_after": "completed_by",
      "in_list_view": 1,
      "in_standard_filter": 1,
      "translatable": 1
    },
    {
      "dt": "Task",
      "fieldtype": "Select",
      "label": "workflow_state",
      "fieldname": "workflow_state",
      "insert_after": "project",
      "options": "Draft\nAcknowledged\nCompleted\nUser Confirmed",
      "hidden": 1,
      "in_standard_filter": 1,
      "translatable": 1
    },
    {
      "dt": "Task",
      "fieldtype": "Data",
      "label": "Contact Mobile No",
      "fieldname": "contact_mobile_no",
      "insert_after": "contact_person",
      "translatable": 1
    },
    {
      "dt": "Task",
      "fieldtype": "Data",
      "label": "Contact Person",
      "fieldname": "contact_person",
      "insert_after": "subject",
      "translatable": 1
    },
    {
      "dt": "Task",
      "fieldtype": "Select",
      "label": "To Department",
      "fieldname": "to_department",
      "options": "Maintenance\nIT",
      "in_standard_filter": 1,
      "translatable": 1
    }
  ],
  "Stock Entry": {
    "dt": "Stock Entry",
    "fieldtype": "Link",
    "label": "Default Difference Account",
    "fieldname": "default_difference_account",
    "insert_after": "source_address_display",
    "options": "Account",
    "mandatory_depends_on": "eval:doc.purpose=='Material Issue' || doc.purpose=='Material Receipt'"
  },
  "Purchase Receipt": {
    "dt": "Purchase Receipt",
    "fieldtype": "Link",
    "label": "Department",
    "fieldname": "department",
    "insert_after": "is_return",
    "options": "Department",
    "read_only": 1
  },
  "Purchase Order": [
    {
      "dt": "Purchase Order",
      "fieldtype": "Long Text",
      "label": "Extra Description",
      "fieldname": "extra_description",
      "insert_after": "items"
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Attach",
      "label": "Comparison Sheet",
      "fieldname": "comparison_sheet",
      "insert_after": "department",
      "Allow in Quick Entry": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Link",
      "label": "Department",
      "fieldname": "department",
      "insert_after": "company",
      "options": "Department",
      "fetch_from": "material_request.department",
      "reqd": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Data",
      "label": "Final Approving Authority",
      "fieldname": "final_approving_authority",
      "insert_after": "first_approving_authority",
      "options": "Email",
      "read_only": 1,
      "translatable": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Data",
      "label": "First Approving Authority",
      "fieldname": "first_approving_authority",
      "insert_after": "recommended_by",
      "options": "Email",
      "read_only": 1,
      "translatable": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Data",
      "label": "Recommended By",
      "fieldname": "recommended_by",
      "insert_after": "alm_column_break",
      "options": "Email",
      "read_only": 1,
      "translatable": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Column Break",
      "fieldname": "alm_column_break",
      "insert_after": "checked_by"
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Data",
      "label": "Checked By",
      "fieldname": "checked_by",
      "insert_after": "prepared_by",
      "options": "Email",
      "read_only": 1,
      "translatable": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Data",
      "label": "Prepared By",
      "fieldname": "prepared_by",
      "insert_after": "alm",
      "options": "Email",
      "read_only": 1,
      "translatable": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Section Break",
      "label": "ALM",
      "fieldname": "alm",
      "insert_after": "schedule_date"
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Data",
      "label": "One Time Vendor Address",
      "fieldname": "one_time_vendor_address",
      "insert_after": "one_time_vendor_section",
      "translatable": 1
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Section Break",
      "label": "One Time Vendor Details",
      "fieldname": "one_time_vendor_section",
      "insert_after": "type",
      "depends_on": "eval: doc.supplier == 'One time Vendor'"
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Select",
      "label": "Type",
      "fieldname": "type",
      "insert_after": "supplier",
      "options": "REVEX\nCAPEX",
      "reqd": 1,
      "in_standard_filter": 1,
      "translatable": 1,
      "description": "Type of Expenditure.\nCAPEX is an amount spent to acquire or improve a long-term asset such as any electronics equipment.\nREVEX refers to expenses incurred in the course of ordinary business, such as sales, general and administrative expenses."
    },
    {
      "dt": "Purchase Order",
      "fieldtype": "Link",
      "label": "Workflow State",
      "fieldname": "workflow_state",
      "options": "Workflow State",
      "hidden": 1,
      "no_copy": 1,
      "allow_on_submit": 1,
      "in_list_view": 1,
      "in_standard_filter": 1
    }
  ],
  "POS Invoice": {
    "dt": "POS Invoice",
    "fieldtype": "Data",
    "label": "Company Abbreviation",
    "fieldname": "company_abbreviation",
    "insert_after": "against_income_account",
    "fetch_from": "company.abbr",
    "hidden": 1,
    "translatable": 1
  },
  "Material Request": [
    {
      "dt": "Material Request",
      "fieldtype": "Link",
      "label": "Material Purchase Link",
      "fieldname": "material_purchase_link",
      "insert_after": "department",
      "options": "Material Request",
      "depends_on": "eval:doc.material_request_type=='Material Issue'",
      "allow_on_submit": 1,
      "permlevel": 2
    },
    {
      "dt": "Material Request",
      "fieldtype": "Link",
      "label": "Department",
      "fieldname": "department",
      "insert_after": "company",
      "options": "Department",
      "reqd": 1
    },
    {
      "dt": "Material Request",
      "fieldtype": "Long Text",
      "label": "Purpose Description",
      "fieldname": "description",
      "insert_after": "purpose",
      "description": "Write down the description of PURPOSE, if detailing is required."
    },
    {
      "dt": "Material Request",
      "fieldtype": "Data",
      "label": "Purpose Subject",
      "fieldname": "purpose",
      "insert_after": "for_a_work_order",
      "reqd": 1,
      "in_standard_filter": 1,
      "translatable": 1
    },
    {
      "dt": "Material Request",
      "fieldtype": "Check",
      "label": "For a Work Order",
      "fieldname": "for_a_work_order",
      "insert_after": "material_request_type",
      "depends_on": "eval:doc.material_request_type == 'Purchase'",
      "in_standard_filter": 1,
      "bold": 1
    },
    {
      "dt": "Material Request",
      "fieldtype": "Check",
      "label": "Completed",
      "fieldname": "completed",
      "insert_after": "naming_series",
      "read_only_depends_on": "eval:doc.completed != user",
      "allow_on_submit": 1
    }
  ],
  "Item Group": [
    {
      "dt": "Item Group",
      "fieldtype": "Int",
      "label": "Live Counter No",
      "fieldname": "live_counter_no",
      "insert_after": "is_group",
      "Non Negative": 1,
      "in_list_view": 1,
      "description": "To be used for Restaurant POS Billing"
    },
    {
      "dt": "Item Group",
      "fieldtype": "Data",
      "label": "Item Code Series",
      "fieldname": "item_code_series",
      "insert_after": "image",
      "mandatory_depends_on": "eval:!doc.is_group",
      "in_list_view": 1,
      "Allow in Quick Entry": 1,
      "translatable": 1
    }
  ],
  "Employee": {
    "dt": "Employee",
    "fieldtype": "Data",
    "label": "Father Or Spouse Name",
    "fieldname": "father_or_spouse_name",
    "insert_after": "employee_name",
    "translatable": 1
  }
}
