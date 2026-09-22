# Changes to Populi's API2 reference

One entry per sync that found a new version of the docs, newest first, written
by `populi-docs sync`. Structural changes only: models, endpoints, fields,
parameters, filters, expands, permissions, webhook events, and which endpoint
descriptions were reworded. Examples are not compared.

<!-- entries -->

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
