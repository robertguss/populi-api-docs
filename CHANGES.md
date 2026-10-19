# Changes to Populi's API2 reference

One entry per sync that found a new version of the docs, newest first, written
by `populi-docs sync`. Structural changes only: models, endpoints, fields,
parameters, filters, expands, permissions, webhook events, and which endpoint
descriptions were reworded. Examples are not compared.

<!-- entries -->

## 2026-10-14 16:35:18 PST

Synced 2026-10-19.

No structural changes (wording or examples only).

## 2026-10-08 16:30:25 PST

Synced 2026-10-12.

### Endpoints

- + `GET /applications/(application)/export_pdf` (Application export_pdf)

### Filter conditions

- + `GET /invoices`: filter `payment_applied_date` (date)
- + `GET /transactions`: filter `invoice_status` (enum)

## 2026-10-05 17:15:39 PST

Synced 2026-10-07.

### Models

- + DigitalResource (`digitalresources`)
- + LibraryResourceCopy (`libraryresourcecopies`)
- + LibraryResourceType (`libraryresourcetypes`)

### Endpoints

- + `DELETE /libraryresources/(libraryresource)` (LibraryResource delete)
- + `DELETE /libraryresources/(libraryresource)/copies/(libraryresourcecopy)/delete` (LibraryResourceCopy delete_copy)
- + `DELETE /libraryresources/(libraryresource)/digitalresources/(digitalresource)/delete` (DigitalResource delete_digital_resource)
- + `DELETE /libraryresources/(libraryresource)/fields/(libraryresourcefield)/delete` (LibraryResource delete_field)
- + `GET /libraryresources/(libraryresource)/copies` (LibraryResourceCopy index (copies))
- + `GET /libraryresources/(libraryresource)/copies/(libraryresourcecopy)` (LibraryResourceCopy show (copy))
- + `GET /libraryresources/(libraryresource)/digitalresources` (DigitalResource index (digital resources))
- + `GET /libraryresources/(libraryresource)/digitalresources/(digitalresource)` (DigitalResource show (digital resource))
- + `GET /libraryresourcetypes` (LibraryResourceType index)
- + `POST /libraryresources` (LibraryResource create)
- + `POST /libraryresources/(libraryresource)/copies/create` (LibraryResourceCopy create_copy)
- + `POST /libraryresources/(libraryresource)/digitalresources/create` (DigitalResource create_digital_resource)
- + `POST /libraryresources/(libraryresource)/digitalresources/upload` (DigitalResource upload file (digital resource))
- + `POST /libraryresources/(libraryresource)/fields/create` (LibraryResource create_field)
- + `POST /libraryresources/(libraryresource)/update_image` (LibraryResource update_image)
- + `PUT /libraryresources/(libraryresource)` (LibraryResource update)
- + `PUT /libraryresources/(libraryresource)/copies/(libraryresourcecopy)/update` (LibraryResourceCopy update_copy)
- + `PUT /libraryresources/(libraryresource)/digitalresources/(digitalresource)/update` (DigitalResource update_digital_resource)
- + `PUT /libraryresources/(libraryresource)/fields/(libraryresourcefield)/update` (LibraryResource update_field)
- − `GET /campuslife/consequences` (StudentConsequence index (campus life))
- − `GET /campuslife/rooms` (Room index (campus life))
- − `GET /campuslife/students` (Person index (campus life))
- − `GET /campuslife/violations` (StudentViolation index (campus life))
- − `GET /webhooks/examples/:trigger_abbrv` (Utilities show example webhook payload)

### Object fields

- + DigitalResource.`added_at` (datetime)
- + DigitalResource.`added_by_id` (int)
- + DigitalResource.`api_version` (--)
- + DigitalResource.`file_id` (int)
- + DigitalResource.`id` (int, required)
- + DigitalResource.`name` (text (255))
- + DigitalResource.`order_id` (int, required)
- + DigitalResource.`resource_id` (int, required)
- + DigitalResource.`sandbox` (bool)
- + DigitalResource.`url` (text (2100))
- + LibraryResourceCopy.`acquisition_date` (date)
- + LibraryResourceCopy.`acquisition_source_id` (int)
- + LibraryResourceCopy.`added_at` (datetime)
- + LibraryResourceCopy.`added_by_id` (int)
- + LibraryResourceCopy.`api_version` (--)
- + LibraryResourceCopy.`barcode` (text (100))
- + LibraryResourceCopy.`call_number` (text (100))
- + LibraryResourceCopy.`current_library_id` (int, required)
- + LibraryResourceCopy.`departed_at` (datetime)
- + LibraryResourceCopy.`destination_library_id` (int)
- + LibraryResourceCopy.`home_library_id` (int, required)
- + LibraryResourceCopy.`id` (int, required)
- + LibraryResourceCopy.`import_id` (int)
- + LibraryResourceCopy.`last_inventoried_at` (datetime)
- + LibraryResourceCopy.`last_inventoried_by_id` (int)
- + LibraryResourceCopy.`last_inventory_location_id` (int)
- + LibraryResourceCopy.`location_id` (int)
- + LibraryResourceCopy.`purchase_price` (decimal)
- + LibraryResourceCopy.`replacement_price` (decimal)
- + LibraryResourceCopy.`resource_id` (int, required)
- + LibraryResourceCopy.`sandbox` (bool)
- + LibraryResourceCopy.`sort_a` (text (100))
- + LibraryResourceCopy.`sort_all` (text (200))
- + LibraryResourceCopy.`sort_b` (decimal)
- + LibraryResourceCopy.`sort_c` (text (50))
- + LibraryResourceCopy.`status` (enum (available, checked_out, lost, deleted, damaged, on_reserve, not_available, on_hold, not_owned), required)
- + LibraryResourceCopy.`status_date` (date)
- + LibraryResourceCopy.`status_link_id` (int)
- + LibraryResourceCopy.`total_loans` (int, required)
- + LibraryResourceType.`abbrv` (text (255))
- + LibraryResourceType.`added_at` (datetime)
- + LibraryResourceType.`api_version` (--)
- + LibraryResourceType.`description` (text (255))
- + LibraryResourceType.`id` (int, required)
- + LibraryResourceType.`image_name` (text (255))
- + LibraryResourceType.`marc_leader_type` (text (10))
- + LibraryResourceType.`name` (text (50), required)
- + LibraryResourceType.`parent_type_id` (int)
- + LibraryResourceType.`plural_name` (text (50), required)
- + LibraryResourceType.`sandbox` (bool)
- + LibraryResourceType.`updated_at` (datetime)

### Filter conditions

- + `GET /paymentdeadlines`: filter `has_active_recurring_payment` (bool)

### Expands

- + `GET /libraryresources`: `digital_resources`
- + `GET /libraryresources/(libraryresource)`: `digital_resources`

### Permissions

- ~ `GET /libraryresources/(libraryresource)`: none → Library Admin, Library Staff

## 2026-09-30 16:36:50 PST

Synced 2026-10-01.

### Expands

- + `GET /aidapplications`: `coa_categories`
- + `GET /people/(person)/aidapplications`: `coa_categories`
- + `GET /people/(person)/aidapplications/(aidapplication)`: `coa_categories`

## 2026-09-29 16:27:55 PST

Synced 2026-09-30.

### Expands

- + `GET /campuslife/students`: `advisors`, `campuses`, `flags`
- + `GET /people`: `advisors`, `campuses`, `flags`
- + `GET /people/(person)`: `advisors`, `campuses`, `flags`
- + `GET /people/by_student_id`: `advisors`, `campuses`, `flags`
- + `GET /people/deleted`: `advisors`, `campuses`, `flags`
- + `GET /programs/(program)/students`: `advisors`, `campuses`, `flags`

## 2026-09-24 16:39:54 PST

Synced 2026-09-26.

### Parameters

- + `GET /coursegroups/(coursegroup)`: parameter `academic_year_id`

## 2026-09-21 11:05:10 PST

First snapshot, synced 2026-09-22: 177 models, 682 endpoints, 97 webhook events.

## Before this copy (hand-written, 2026-09-22)

Compared by hand against the copy in `wts-lx/lx_data_lake/docs/api_docs/populi/`
(synced 2026-08-04 from Populi's docs of 2026-07-31), on endpoints, object
fields, and filter conditions. Descriptions were not compared.

- Models: + LtiTool, + MeetingTime, + Webhooks (the page).
- Endpoints: + `GET /people/deleted`, + `GET /organizations/deleted`,
  + `GET /users/deleted`, + `GET /custominfodata/deleted`,
  + `GET /users/(user)/hard_delete`, + `GET /ltitools`,
  + `GET /ltitools/(ltitool)`, + meeting times on course offerings (`GET`,
  `POST`, `PUT`, `DELETE` under `/courseofferings/(courseoffering)/meetingtimes`),
  which replace − `GET /courseofferings/(courseoffering)/coursemeetings/(coursemeeting)`.
- Filter conditions: + `deleted_at` on `GET /people`, `GET /organizations`,
  and `GET /custominfodata`; + six on `GET /users` (`added_at`, `deleted_at`,
  `is_active`, `last_activity_at`, `login_type`, `username`).
- Object fields: + AidDisbursement.`cod_payment_period_end_date`,
  + Assignment.`added_at` and `added_by_id`, + ISIR.`comment_codes`,
  + LockType.`added_at`, `added_by_id`, `type`; the CustomInfoField object's
  fields are now documented.
