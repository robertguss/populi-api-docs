# Populi API2: every endpoint

> A local copy of Populi's API2 reference (https://populi.co/api/), rebuilt for agents by `populi-docs`. Do not edit by hand; run `populi-docs sync` to refresh. Docs version: 2026-09-21 11:05:10 PST. 682 endpoints, sorted by path. Paths are relative to `https://<school>.populiweb.com/api2`; `(name)` is an id in the path.

| Method | Path | Action | Model | Summary |
|---|---|---|---|---|
| GET | `/academicterms` | index | [AcademicTerm](models/academicterms.md) | Retrieves all AcademicTerm objects. |
| GET | `/academicterms/(academicterm)` | show | [AcademicTerm](models/academicterms.md) | Retrieves a specific AcademicTerm object. |
| GET | `/academicterms/(academicterm)/academicprogress` | academicprogress | [AcademicTerm](models/academicterms.md) | Returns the equivalent of the Financial Aid Academic Progress Report. |
| GET | `/academicterms/(academicterm)/billing` | billing | [AcademicTerm](models/academicterms.md) | Returns a variety of collected individual student billing information for a specified term. |
| GET | `/academicterms/(academicterm)/courseofferings` | courseofferings | [AcademicTerm](models/academicterms.md) |  |
| GET | `/academicterms/(academicterm)/enrollments` | enrollments | [AcademicTerm](models/academicterms.md) |  |
| GET | `/academicterms/(academicterm)/students` | students | [AcademicTerm](models/academicterms.md) |  |
| GET | `/academicterms/(academicterm)/waitinglist` | waitinglist | [AcademicTerm](models/academicterms.md) |  |
| GET | `/academicterms/current` | current | [AcademicTerm](models/academicterms.md) | Returns the current default term. |
| GET | `/academictermtypes` | index | [AcademicTermType](models/academictermtypes.md) | Retrieves all AcademicTermType objects. |
| GET | `/academicyears` | index | [AcademicYear](models/academicyears.md) | Retrieves all AcademicYear objects. |
| GET | `/academicyears/(academicyear)` | show | [AcademicYear](models/academicyears.md) | Retrieves a specific AcademicYear object. |
| GET | `/academicyears/current` | current | [AcademicYear](models/academicyears.md) |  |
| GET | `/accounts` | index | [Account](models/accounts.md) | Retrieves all Account objects. |
| GET | `/accounts/(account)` | show | [Account](models/accounts.md) | Retrieves a specific Account object. |
| GET | `/admissionscustominfofields` | index (admissions) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the admissions type. |
| GET | `/admissionscustominfofields/(admissionscustominfofield)` | show (admissions) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the admissions type. |
| GET | `/advisees` | index | [Advisee](models/advisees.md) | Retrieves all Advisee objects that match given filter conditions. |
| GET | `/aidapplications` | index | [AidApplication](models/aidapplications.md) | Retrieves all AidApplication objects that match given filter conditions. |
| GET | `/aidauthorizations` | index | [AidAuthorization](models/aidauthorizations.md) | Retrieves all AidAuthorization objects. |
| GET | `/aidauthorizations/(aidauthorization)` | show | [AidAuthorization](models/aidauthorizations.md) | Retrieves a specific AidAuthorization object. |
| GET | `/aidawards` | index | [AidAward](models/aidawards.md) | Retrieves all AidAward objects that match given filter conditions. |
| GET | `/aidclassifications` | index | [AidClassification](models/aidclassifications.md) | Retrieves all AidClassification objects. |
| GET | `/aidclassifications/(aidclassification)` | show | [AidClassification](models/aidclassifications.md) | Retrieves a specific AidClassification object. |
| GET | `/aiddisbursementbatches` | index | [AidDisbursementBatch](models/aiddisbursementbatches.md) | Retrieves all AidDisbursementBatch objects that match given filter conditions. |
| POST | `/aiddisbursementbatches` | create | [AidDisbursementBatch](models/aiddisbursementbatches.md) | Creates a new AidDisbursementBatch object. |
| GET | `/aiddisbursementbatches/(aiddisbursementbatch)` | show | [AidDisbursementBatch](models/aiddisbursementbatches.md) | Retrieves a specific AidDisbursementBatch object. |
| GET | `/aiddisbursements` | index | [AidDisbursement](models/aiddisbursements.md) | Retrieves all AidDisbursement objects that match given filter conditions. |
| GET | `/aidtypes` | index | [AidType](models/aidtypes.md) | Retrieves all AidType objects. |
| GET | `/aidtypes/(aidtype)` | show | [AidType](models/aidtypes.md) | Retrieves a specific AidType object. |
| GET | `/aidyears` | index | [AidYear](models/aidyears.md) | Retrieves all AidYear objects. |
| GET | `/aidyears/(aidyear)` | show | [AidYear](models/aidyears.md) | Retrieves a specific AidYear object. |
| GET | `/aidyears/(aidyear)/schedules` | index | [AidYearSchedule](models/aidyearschedules.md) | Retrieves all AidYearSchedule objects tied to a specific Aidyear. |
| GET | `/aidyears/(aidyear)/schedules/(aidyearschedule)` | show | [AidYearSchedule](models/aidyearschedules.md) | Retrieves a specific AidYearSchedule object. |
| GET | `/appealmedia` | index | [AppealMedium](models/appealmedia.md) | Retrieves all AppealMedium objects. |
| GET | `/appealmedia/(appealmedium)` | show | [AppealMedium](models/appealmedia.md) | Retrieves a specific AppealMedium object. |
| GET | `/appeals` | index | [Appeal](models/appeals.md) | Retrieves all Appeal objects. |
| GET | `/appeals/(appeal)` | show | [Appeal](models/appeals.md) | Retrieves a specific Appeal object. |
| GET | `/applications` | index | [Application](models/applications.md) | Retrieves all Application objects that match given filter conditions. |
| POST | `/applications` | create | [Application](models/applications.md) | Creates a new Application object. |
| DELETE | `/applications/(application)` | delete | [Application](models/applications.md) | Deletes an existing Application object. |
| GET | `/applications/(application)` | show | [Application](models/applications.md) | Retrieves a specific Application object. |
| PUT | `/applications/(application)` | update | [Application](models/applications.md) | Updates an existing Application object. |
| GET | `/applications/(application)/fields` | fields | [Application](models/applications.md) |  |
| GET | `/applications/(application)/link_to_person` | link_to_person | [Application](models/applications.md) |  |
| GET | `/applications/(application)/submit` | submit | [Application](models/applications.md) |  |
| GET | `/applications/(application)/unlink_person` | unlink_person | [Application](models/applications.md) |  |
| GET | `/applicationtemplates` | index | [ApplicationTemplate](models/applicationtemplates.md) | Retrieves all ApplicationTemplate objects. |
| GET | `/applicationtemplates/(applicationtemplate)` | show | [ApplicationTemplate](models/applicationtemplates.md) | Retrieves a specific ApplicationTemplate object. |
| GET | `/attendance/detail` | index | [CourseAttendance](models/attendancereports.md) | Retrieves all CourseAttendance objects that match given filter conditions. |
| GET | `/automationhandler/(automationhandler)` | show | [AutomationHandler](models/triggerhandlers.md) | Retrieves a specific AutomationHandler object. |
| GET | `/automationhandlers` | index | [AutomationHandler](models/triggerhandlers.md) | Retrieves all AutomationHandler objects. |
| GET | `/automations` | index | [Automation](models/triggers.md) | Retrieves all Automation objects. |
| GET | `/automations/(automation)` | show | [Automation](models/triggers.md) | Retrieves a specific Automation object. |
| GET | `/backups` | index | [Backup](models/customerbackups.md) | Retrieves all Backup objects. |
| GET | `/backups/(backup)` | show | [Backup](models/customerbackups.md) | Retrieves a specific Backup object. |
| GET | `/backups/(backup)/download` | download | [Backup](models/customerbackups.md) |  |
| GET | `/backups/most_recent_completed` | most_recent_completed | [Backup](models/customerbackups.md) |  |
| POST | `/backups/request` | request | [Backup](models/customerbackups.md) |  |
| GET | `/buildings` | index | [Building](models/buildings.md) | Retrieves all Building objects. |
| GET | `/buildings/(building)` | show | [Building](models/buildings.md) | Retrieves a specific Building object. |
| GET | `/campaigns` | index | [Campaign](models/campaigns.md) | Retrieves all Campaign objects. |
| GET | `/campaigns/(campaign)` | show | [Campaign](models/campaigns.md) | Retrieves a specific Campaign object. |
| GET | `/campuses` | index | [Campus](models/campuses.md) | Retrieves all Campus objects. |
| GET | `/campuses/(campus)` | show | [Campus](models/campuses.md) | Retrieves a specific Campus object. |
| GET | `/campuslife/consequences` | index (campus life) | [StudentConsequence](models/studentconsequences.md) | Retrieves all StudentConsequence objects that match given filter conditions. |
| GET | `/campuslife/rooms` | index (campus life) | [Room](models/rooms.md) | Retrieves all Room objects that match given filter conditions. |
| GET | `/campuslife/students` | index (campus life) | [Person](models/people.md) | Retrieves all Person objects that match given filter conditions. |
| GET | `/campuslife/violations` | index (campus life) | [StudentViolation](models/studentviolations.md) | Retrieves all StudentViolation objects that match given filter conditions. |
| GET | `/campuslifecustominfofields` | index (campus life) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the campus life type. |
| GET | `/campuslifecustominfofields/(campuslifecustominfofield)` | show (campus life) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the campus life type. |
| GET | `/canadiandonationreceipts/(canadiandonationreceipt)` | show | [CanadianDonationReceipt](models/canadiandonationreceipts.md) | Retrieves a specific CanadianDonationReceipt object. |
| GET | `/catalogcourses` | index | [CatalogCourse](models/catalogcourses.md) | Retrieves all CatalogCourse objects that match given filter conditions. |
| GET | `/catalogcourses/(catalogcourse)` | show | [CatalogCourse](models/catalogcourses.md) | Retrieves a specific CatalogCourse object. |
| GET | `/catalogcourses/(catalogcourse)/questioncategories` | index | [QuestionCategory](models/questioncategories.md) | Retrieves all QuestionCategory objects tied to a specific Catalogcourse. |
| GET | `/catalogcourses/(catalogcourse)/questioncategories/(questioncategory)` | show | [QuestionCategory](models/questioncategories.md) | Retrieves a specific QuestionCategory object. |
| GET | `/catalogcourses/(catalogcourse)/questions` | index | [Question](models/questions.md) | Retrieves all Question objects tied to a specific Catalogcourse. |
| GET | `/catalogcourses/(catalogcourse)/questions/(question)` | show | [Question](models/questions.md) | Retrieves a specific Question object. |
| GET | `/changelog` | changelog | [ChangeLog](models/account.md) | Results are limited to changes in the past 30 days. |
| GET | `/checks` | index | [Check](models/checks.md) | Retrieves all Check objects that match given filter conditions. |
| GET | `/checks/(check)` | show | [Check](models/checks.md) | Retrieves a specific Check object. |
| GET | `/coacategories` | index | [COACategory](models/coacategories.md) | Retrieves all COACategory objects. |
| GET | `/coacategories/(coacategory)` | show | [COACategory](models/coacategories.md) | Retrieves a specific COACategory object. |
| GET | `/communicationplans` | index | [CommunicationPlan](models/communicationplans.md) | Retrieves all CommunicationPlan objects. |
| GET | `/communicationplans/(communicationplan)` | show | [CommunicationPlan](models/communicationplans.md) | Retrieves a specific CommunicationPlan object. |
| GET | `/consequences` | index | [Consequence](models/consequences.md) | Retrieves all Consequence objects. |
| GET | `/consequences/(consequence)` | show | [Consequence](models/consequences.md) | Retrieves a specific Consequence object. |
| GET | `/countries` | index | [Country](models/countries.md) | Retrieves all Country objects. |
| GET | `/coursedeliverymethods` | index | [CourseDeliveryMethod](models/coursedeliverymethods.md) | Retrieves all CourseDeliveryMethod objects. |
| GET | `/coursedeliverymethods/(coursedeliverymethod)` | show | [CourseDeliveryMethod](models/coursedeliverymethods.md) | Retrieves a specific CourseDeliveryMethod object. |
| GET | `/courseevaluations` | index | [CourseEvaluation](models/courseevaluations.md) | Retrieves all CourseEvaluation objects. |
| GET | `/courseevaluations/(courseevaluation)` | show | [CourseEvaluation](models/courseevaluations.md) | Retrieves a specific CourseEvaluation object. |
| GET | `/courseevaluations/(courseevaluation)/answers` | answers | [CourseEvaluation](models/courseevaluations.md) |  |
| GET | `/coursegrouprequirements` | index | [CourseGroupRequirement](models/coursegrouprequirements.md) | Retrieves all CourseGroupRequirement objects. |
| GET | `/coursegrouprequirements/(coursegrouprequirement)` | show | [CourseGroupRequirement](models/coursegrouprequirements.md) | Retrieves a specific CourseGroupRequirement object. |
| GET | `/coursegroups` | index | [CourseGroup](models/coursegroups.md) | Retrieves all CourseGroup objects. |
| GET | `/coursegroups/(coursegroup)` | show | [CourseGroup](models/coursegroups.md) | Retrieves a specific CourseGroup object. |
| GET | `/courselessons/(courselesson)/links` | index (courselesson) | [Link](models/links.md) | Retrieves all Links from a course lesson. |
| DELETE | `/courselessons/(courselesson)/links/(link)` | delete (courselesson) | [Link](models/links.md) | Deletes a specific Link from a course lesson. |
| GET | `/courselessons/(courselesson)/links/(link)` | show (courselesson) | [Link](models/links.md) | Retrieves a specific Link from a course lesson. |
| PUT | `/courselessons/(courselesson)/links/(link)` | update (courselesson) | [Link](models/links.md) | Updates a specific Link in a course lesson. |
| GET | `/courseofferings` | index | [CourseOffering](models/courseofferings.md) | Retrieves all CourseOffering objects that match given filter conditions. |
| GET | `/courseofferings/(courseoffering)` | show | [CourseOffering](models/courseofferings.md) | Retrieves a specific CourseOffering object. |
| GET | `/courseofferings/(courseoffering)/assignmentgroups` | index | [AssignmentGroup](models/assignmentgroups.md) | Retrieves all AssignmentGroup objects tied to a specific Courseoffering. |
| POST | `/courseofferings/(courseoffering)/assignmentgroups` | create | [AssignmentGroup](models/assignmentgroups.md) | Creates a new AssignmentGroup object. |
| DELETE | `/courseofferings/(courseoffering)/assignmentgroups/(assignmentgroup)` | delete | [AssignmentGroup](models/assignmentgroups.md) | Deletes an existing AssignmentGroup object. |
| GET | `/courseofferings/(courseoffering)/assignmentgroups/(assignmentgroup)` | show | [AssignmentGroup](models/assignmentgroups.md) | Retrieves a specific AssignmentGroup object. |
| PUT | `/courseofferings/(courseoffering)/assignmentgroups/(assignmentgroup)` | update | [AssignmentGroup](models/assignmentgroups.md) | Updates an existing AssignmentGroup object. |
| GET | `/courseofferings/(courseoffering)/assignments` | index | [Assignment](models/courseassignments.md) | Retrieves all Assignment objects tied to a specific Courseoffering. |
| POST | `/courseofferings/(courseoffering)/assignments` | create | [Assignment](models/courseassignments.md) | Creates a new Assignment object. |
| DELETE | `/courseofferings/(courseoffering)/assignments/(assignment)` | delete | [Assignment](models/courseassignments.md) | Deletes an existing Assignment object. |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)` | show | [Assignment](models/courseassignments.md) | Retrieves a specific Assignment object. |
| PUT | `/courseofferings/(courseoffering)/assignments/(assignment)` | update | [Assignment](models/courseassignments.md) | Updates an existing Assignment object. |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/students/(person)/comments` | comments | [AssignmentSubmission](models/assignmentsubmissions.md) |  |
| POST | `/courseofferings/(courseoffering)/assignments/(assignment)/students/(person)/comments/create` | create_comment | [AssignmentSubmission](models/assignmentsubmissions.md) |  |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/students/(person)/grade` | show | [AssignmentGrade](models/assignmentgrades.md) | Retrieves a specific AssignmentGrade object. |
| PUT | `/courseofferings/(courseoffering)/assignments/(assignment)/students/(person)/grade/update` | update | [AssignmentGrade](models/assignmentgrades.md) | Updates an existing AssignmentGrade object. |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/students/(person)/rubric_scores` | rubric_scores | [Assignment](models/courseassignments.md) |  |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/submissions` | index | [AssignmentSubmission](models/assignmentsubmissions.md) | Retrieves all AssignmentSubmission objects tied to a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/submissions/(person)` | index (person) | [AssignmentSubmission](models/assignmentsubmissions.md) | Retrieves all AssignmentSubmission objects tied to a specific Courseoffering. |
| POST | `/courseofferings/(courseoffering)/assignments/(assignment)/submissions/(person)` | create | [AssignmentSubmission](models/assignmentsubmissions.md) | Creates a new AssignmentSubmission object. |
| DELETE | `/courseofferings/(courseoffering)/assignments/(assignment)/submissions/(person)/(assignmentsubmission)` | delete | [AssignmentSubmission](models/assignmentsubmissions.md) | Deletes an existing AssignmentSubmission object. |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/submissions/(person)/(assignmentsubmission)` | show | [AssignmentSubmission](models/assignmentsubmissions.md) | Retrieves a specific AssignmentSubmission object. |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/testinstances` | index | [AssignmentTestInstance](models/assignmenttestinstance.md) | Retrieves all AssignmentTestInstance objects (test submissions), tied to specific test Assignment in a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/assignments/(assignment)/testinstances/(person)` | index (person) | [AssignmentTestInstance](models/assignmenttestinstance.md) | Retrieves all AssignmentTestInstance objects (test submissions), tied to specific test Assignment and a specific Person in a specific Cours… |
| GET | `/courseofferings/(courseoffering)/calendar` | calendar | [CourseOffering](models/courseofferings.md) |  |
| GET | `/courseofferings/(courseoffering)/coursemeetings` | index | [CourseMeeting](models/coursemeetings.md) | Retrieves all CourseMeeting objects tied to a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/files` | index (courseoffering) | [File](models/files.md) | Retrieves all File objects tied to a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/files/(file)` | show (courseoffering) | [File](models/files.md) | Retrieves a specific File object. |
| POST | `/courseofferings/(courseoffering)/finalize` | finalize | [CourseOffering](models/courseofferings.md) |  |
| GET | `/courseofferings/(courseoffering)/lessons` | index | [CourseLesson](models/courselessons.md) | Retrieves all CourseLesson objects tied to a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/lessons/(courselesson)` | show | [CourseLesson](models/courselessons.md) | Retrieves a specific CourseLesson object. |
| GET | `/courseofferings/(courseoffering)/lessons/(courselesson)/files` | index (courselesson) | [File](models/files.md) | Retrieves all File objects tied to a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/lessons/(courselesson)/files/(file)` | show (courselesson) | [File](models/files.md) | Retrieves a specific File object. |
| GET | `/courseofferings/(courseoffering)/lessons/(courselesson)/pages` | index | [LessonPage](models/lessonpages.md) | Retrieves all LessonPage objects tied to a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/lessons/(courselesson)/pages/(lessonpage)` | show | [LessonPage](models/lessonpages.md) | Retrieves a specific LessonPage object. |
| GET | `/courseofferings/(courseoffering)/links` | index (syllabus and lessons) | [Link](models/links.md) | Retrieves all Links from the course syllabus page and course lessons. |
| POST | `/courseofferings/(courseoffering)/links` | create (syllabus) | [Link](models/links.md) | Creates a new Link on the course syllabus page. |
| DELETE | `/courseofferings/(courseoffering)/links/(link)` | delete (syllabus) | [Link](models/links.md) | Deletes a Link from the course syllabus page. |
| GET | `/courseofferings/(courseoffering)/links/(link)` | show (syllabus) | [Link](models/links.md) | Retrieves a specific Link from the course syllabus page. |
| PUT | `/courseofferings/(courseoffering)/links/(link)` | update (syllabus) | [Link](models/links.md) | Updates a Link on the course syllabus page. |
| GET | `/courseofferings/(courseoffering)/meetingtimes` | index | [MeetingTime](models/courseschedules.md) | Retrieves all MeetingTime objects tied to a specific Courseoffering. |
| POST | `/courseofferings/(courseoffering)/meetingtimes` | create | [MeetingTime](models/courseschedules.md) | Creates a new MeetingTime object. |
| DELETE | `/courseofferings/(courseoffering)/meetingtimes/(meetingtime)` | delete | [MeetingTime](models/courseschedules.md) | Deletes an existing MeetingTime object. |
| GET | `/courseofferings/(courseoffering)/meetingtimes/(meetingtime)` | show | [MeetingTime](models/courseschedules.md) | Retrieves a specific MeetingTime object. |
| PUT | `/courseofferings/(courseoffering)/meetingtimes/(meetingtime)` | update | [MeetingTime](models/courseschedules.md) | Updates an existing MeetingTime object. |
| GET | `/courseofferings/(courseoffering)/posts` | index (courseoffering) | [Post](models/bulletinboardposts.md) | Retrieves all Post objects tied to a specific Courseoffering. |
| POST | `/courseofferings/(courseoffering)/posts` | create (courseoffering) | [Post](models/bulletinboardposts.md) | Creates a new Post object. |
| DELETE | `/courseofferings/(courseoffering)/posts/(post)` | delete (courseoffering) | [Post](models/bulletinboardposts.md) | Deletes an existing Post object. |
| GET | `/courseofferings/(courseoffering)/posts/(post)` | show (courseoffering) | [Post](models/bulletinboardposts.md) | Retrieves a specific Post object. |
| PUT | `/courseofferings/(courseoffering)/posts/(post)` | update (courseoffering) | [Post](models/bulletinboardposts.md) | Updates an existing Post object. |
| GET | `/courseofferings/(courseoffering)/students` | index (courseoffering) | [Enrollment](models/coursestudents.md) | Retrieves all Enrollment objects tied to a specific Courseoffering. |
| GET | `/courseofferings/(courseoffering)/students/(enrollment)` | show (courseoffering) | [Enrollment](models/coursestudents.md) | Retrieves a specific Enrollment object. |
| GET | `/courseofferings/(courseoffering)/students/(enrollment)/attendance` | attendance | [Enrollment](models/coursestudents.md) |  |
| PUT | `/courseofferings/(courseoffering)/students/(enrollment)/attendance/update` | update_attendance | [CourseMeeting](models/coursemeetings.md) | Updates the attendance attribute of an existing CourseMeeting object. |
| GET | `/courseofferings/(courseoffering)/students/(enrollment)/finalize` | finalize | [Enrollment](models/coursestudents.md) |  |
| PUT | `/courseofferings/(courseoffering)/students/(enrollment)/update_final_grade` | update_final_grade | [Enrollment](models/coursestudents.md) | Updates the final_grade attribute of an existing Enrollment object. |
| GET | `/courseofferings/(courseoffering)/syllabus` | syllabus | [CourseOffering](models/courseofferings.md) |  |
| GET | `/credits` | index | [Credit](models/credits.md) | Retrieves all Credit objects that match given filter conditions. |
| GET | `/credits/(credit)` | show | [Credit](models/credits.md) | Retrieves a specific Credit object. |
| GET | `/custominfodata` | index (all types) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects of all types. |
| GET | `/custominfodata/deleted` | deleted | [CustomInfoData](models/custominfodata.md) | Retrieves deleted CustomInfoData objects. |
| GET | `/dataslicerreports` | index | [DataSlicerReport](models/dataslicerreports.md) | Retrieves all DataSlicerReport objects. |
| GET | `/dataslicerreports/(dataslicerreport)` | show | [DataSlicerReport](models/dataslicerreports.md) | Retrieves a specific DataSlicerReport object. |
| GET | `/dataslicerreports/(dataslicerreport)/results` | results | [DataSlicerReport](models/dataslicerreports.md) | Runs the specified Data Slicer report and returns the results as XLS, CSV, or JSON. |
| GET | `/declinedreasons` | index | [DeclinedReason](models/declinedreasons.md) | Retrieves all DeclinedReason objects. |
| GET | `/declinedreasons/(declinedreason)` | show | [DeclinedReason](models/declinedreasons.md) | Retrieves a specific DeclinedReason object. |
| GET | `/degreelevels` | index | [DegreeLevel](models/degreelevels.md) | Retrieves all DegreeLevel objects. |
| GET | `/degreelevels/(degreelevel)` | show | [DegreeLevel](models/degreelevels.md) | Retrieves a specific DegreeLevel object. |
| GET | `/degreelevels/(degreelevel)/students` | students | [DegreeLevel](models/degreelevels.md) |  |
| GET | `/degrees` | index | [Degree](models/degrees.md) | Retrieves all Degree objects that match given filter conditions. |
| GET | `/degrees/(degree)` | show | [Degree](models/degrees.md) | Retrieves a specific Degree object. |
| GET | `/degrees/(degree)/specializations` | index | [Specialization](models/specializations.md) | Retrieves all Specialization objects tied to a specific Degree. |
| GET | `/degrees/(degree)/specializations/(specialization)` | show | [Specialization](models/specializations.md) | Retrieves a specific Specialization object. |
| GET | `/degrees/(degree)/specializations/(specialization)/students` | students | [Specialization](models/specializations.md) |  |
| GET | `/degrees/(degree)/students` | students | [Degree](models/degrees.md) |  |
| GET | `/departments` | index | [Department](models/departments.md) | Retrieves all Department objects. |
| GET | `/departments/(department)` | show | [Department](models/departments.md) | Retrieves a specific Department object. |
| GET | `/disciplinetypes` | index | [DisciplineType](models/disciplinetypes.md) | Retrieves all DisciplineType objects. |
| GET | `/disciplinetypes/(disciplinetype)` | show | [DisciplineType](models/disciplinetypes.md) | Retrieves a specific DisciplineType object. |
| GET | `/discountcodes` | index | [BookstoreDiscountCode](models/bookstorediscountcodes.md) | Retrieves all BookstoreDiscountCode objects that match given filter conditions. |
| GET | `/discountcodes/(bookstorediscountcode)` | show | [BookstoreDiscountCode](models/bookstorediscountcodes.md) | Retrieves a specific BookstoreDiscountCode object. |
| GET | `/donatepages` | index | [DonatePage](models/donatepages.md) | Retrieves all DonatePage objects. |
| GET | `/donatepages/(donatepage)` | show | [DonatePage](models/donatepages.md) | Retrieves a specific DonatePage object. |
| GET | `/donationcustominfofields` | index (donation) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the donation type. |
| GET | `/donationcustominfofields/(donationcustominfofield)` | show (donation) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the donation type. |
| GET | `/donations` | index | [Donation](models/donations.md) | Retrieves all Donation objects that match given filter conditions. |
| POST | `/donations` | create | [Donation](models/donations.md) | Creates a new Donation object. |
| GET | `/donations/(donation)` | show | [Donation](models/donations.md) | Retrieves a specific Donation object. |
| PUT | `/donations/(donation)` | update | [Donation](models/donations.md) | Updates an existing Donation object. |
| POST | `/donations/(donation)/custominfodata` | create (donation) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, tied to a specified Donation object. |
| GET | `/donations/(donation)/custominfodata/` | index (donation) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Donation, tied to a specified Donation object. |
| DELETE | `/donations/(donation)/custominfodata/(custominfodata)` | delete (donation) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, tied to a specified Donation object. |
| GET | `/donations/(donation)/custominfodata/(custominfodata)` | show (donation) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, tied to a specified Donation object. |
| PUT | `/donations/(donation)/custominfodata/(custominfodata)` | update (donation) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, tied to a specified Donation object. |
| GET | `/donations/(donation)/link_to_owner` | link_to_owner | [Donation](models/donations.md) |  |
| GET | `/donations/(donation)/unlink_donor` | unlink_donor | [Donation](models/donations.md) |  |
| GET | `/donations/(donation)/unlink_soft_credit` | unlink_soft_credit | [Donation](models/donations.md) |  |
| GET | `/donations/recurring` | recurring | [Donation](models/donations.md) |  |
| GET | `/donorcustominfofields` | index (donor) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the donor type. |
| GET | `/donorcustominfofields/(donorcustominfofield)` | show (donor) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the donor type. |
| GET | `/donors` | index | [Donor](models/donors.md) | Retrieves all Donor objects that match given filter conditions. |
| GET | `/donors/(donor)` | show | [Donor](models/donors.md) | Retrieves a specific Donor object. |
| POST | `/donors/(donor)/custominfodata` | create (donor) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, tied to a specified Donor object. |
| GET | `/donors/(donor)/custominfodata/` | index (donor) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Donor, tied to a specified Donor object. |
| DELETE | `/donors/(donor)/custominfodata/(custominfodata)` | delete (donor) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, tied to a specified Donor object. |
| GET | `/donors/(donor)/custominfodata/(custominfodata)` | show (donor) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, tied to a specified Donor object. |
| PUT | `/donors/(donor)/custominfodata/(custominfodata)` | update (donor) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, tied to a specified Donor object. |
| GET | `/educationlevels` | index | [EducationLevel](models/educationlevels.md) | Retrieves all EducationLevel objects. |
| GET | `/educationlevels/(educationlevel)` | show | [EducationLevel](models/educationlevels.md) | Retrieves a specific EducationLevel object. |
| POST | `/emailaddresses/resubscribe` | resubscribe | [EmailAddress](models/emailaddresses.md) |  |
| POST | `/emailaddresses/unsubscribe` | unsubscribe | [EmailAddress](models/emailaddresses.md) |  |
| GET | `/emailtemplates` | index | [EmailTemplate](models/emailtemplates.md) | Retrieves all EmailTemplate objects. |
| GET | `/emailtemplates/(emailtemplate)` | show | [EmailTemplate](models/emailtemplates.md) | Retrieves a specific EmailTemplate object. |
| GET | `/enrollmentagreements` | index | [EnrollmentAgreement](models/enrollmentagreements.md) | Retrieves all EnrollmentAgreement objects that match given filter conditions. |
| GET | `/enrollmentagreements/(enrollmentagreement)` | show | [EnrollmentAgreement](models/enrollmentagreements.md) | Retrieves a specific EnrollmentAgreement object. |
| GET | `/enrollments` | index | [Enrollment](models/coursestudents.md) | Retrieves all Enrollment objects that match given filter conditions. |
| GET | `/events` | index | [CalendarEvent](models/calendarevents.md) | Returns up to 200 events per page. |
| POST | `/events` | create | [CalendarEvent](models/calendarevents.md) | Creates a new CalendarEvent object. |
| DELETE | `/events/(calendarevent)` | delete | [CalendarEvent](models/calendarevents.md) | Deletes an existing CalendarEvent object. |
| GET | `/events/(calendarevent)` | show | [CalendarEvent](models/calendarevents.md) | Retrieves a specific CalendarEvent object. |
| PUT | `/events/(calendarevent)` | update | [CalendarEvent](models/calendarevents.md) | Updates an existing CalendarEvent object. |
| GET | `/exitreasons` | index | [ExitReason](models/exitreasons.md) | Retrieves all ExitReason objects. |
| GET | `/exitreasons/(exitreason)` | show | [ExitReason](models/exitreasons.md) | Retrieves a specific ExitReason object. |
| GET | `/fees` | index | [Fee](models/fees.md) | Retrieves all Fee objects. |
| GET | `/fees/(fee)` | show | [Fee](models/fees.md) | Retrieves a specific Fee object. |
| GET | `/files/(file)` | show | [File](models/files.md) | Retrieves a specific File object. |
| GET | `/files/(file)/download` | download | [File](models/files.md) |  |
| GET | `/files/(file)/download_link` | download_link | [File](models/files.md) |  |
| GET | `/financialaidcustominfofields` | index (financial aid) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the financial aid type. |
| GET | `/financialaidcustominfofields/(financialaidcustominfofield)` | show (financial aid) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the financial aid type. |
| GET | `/financialcustominfofields` | index (financial) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the financial type. |
| GET | `/financialcustominfofields/(financialcustominfofield)` | show (financial) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the financial type. |
| GET | `/forms` | index | [Form](models/forms.md) | Retrieves all Form objects that match given filter conditions. |
| GET | `/forms/(form)` | show | [Form](models/forms.md) | Retrieves a specific Form object. |
| GET | `/forms/(form)/responses` | index | [FormResponse](models/formresponses.md) | Retrieves all FormResponse objects that match given filter conditions. |
| GET | `/forms/(form)/responses/(formresponse)` | show | [FormResponse](models/formresponses.md) | Retrieves a specific FormResponse object. |
| GET | `/forms/(form)/responses/(formresponse)/link_to_person` | link_to_person | [FormResponse](models/formresponses.md) |  |
| GET | `/forms/(form)/responses/(formresponse)/unlink_person` | unlink_person | [FormResponse](models/formresponses.md) |  |
| PUT | `/forms/(form)/responses/(formresponse)/update_status` | update_status | [FormResponse](models/formresponses.md) | The status of a FormReponse can only be set to certain states, depending on the context. |
| GET | `/funds` | index | [Fund](models/funds.md) | Retrieves all Fund objects. |
| GET | `/funds/(fund)` | show | [Fund](models/funds.md) | Retrieves a specific Fund object. |
| GET | `/gradescales` | index | [GradeScale](models/gradescales.md) | Retrieves all GradeScale objects. |
| GET | `/gradescales/(gradescale)` | show | [GradeScale](models/gradescales.md) | Retrieves a specific GradeScale object. |
| GET | `/groups` | index | [Group](models/groups.md) | Retrieves all Group objects that match given filter conditions. |
| GET | `/groups/(group)` | show | [Group](models/groups.md) | Retrieves a specific Group object. |
| GET | `/groups/(group)/posts` | index (group) | [Post](models/bulletinboardposts.md) | Retrieves all Post objects tied to a specific Group. |
| GET | `/groups/(group)/posts/(post)` | show (group) | [Post](models/bulletinboardposts.md) | Retrieves a specific Post object. |
| GET | `/honors` | index | [Honor](models/honors.md) | Retrieves all Honor objects. |
| GET | `/honors/(honor)` | show | [Honor](models/honors.md) | Retrieves a specific Honor object. |
| GET | `/idcardtemplates` | index | [IDCardTemplate](models/idcardtemplates.md) | Retrieves all IDCardTemplate objects. |
| GET | `/idcardtemplates/printlayouts` | index (PrintLayouts) | [IDCardTemplate](models/idcardtemplates.md) | Retrieves all IdCardTemplate objects. |
| GET | `/inquiries` | index | [Inquiry](models/inquiries.md) | Retrieves all Inquiry objects that match given filter conditions. |
| POST | `/inquiries` | create | [Inquiry](models/inquiries.md) | Creates a new Inquiry object. |
| DELETE | `/inquiries/(inquiry)` | delete | [Inquiry](models/inquiries.md) | Deletes an existing Inquiry object. |
| GET | `/inquiries/(inquiry)` | show | [Inquiry](models/inquiries.md) | Retrieves a specific Inquiry object. |
| PUT | `/inquiries/(inquiry)` | update | [Inquiry](models/inquiries.md) | Updates an existing Inquiry object. |
| GET | `/inquiries/(inquiry)/link_to_person` | link_to_person | [Inquiry](models/inquiries.md) |  |
| GET | `/inventorybatches` | index | [InventoryBatch](models/inventorybatches.md) | Retrieves all InventoryBatch objects. |
| GET | `/inventorybatches/(inventorybatch)` | show | [InventoryBatch](models/inventorybatches.md) | Retrieves a specific InventoryBatch object. |
| GET | `/invoices` | index | [Invoice](models/invoices.md) | Retrieves all Invoice objects that match given filter conditions. |
| GET | `/invoices/(invoice)` | show | [Invoice](models/invoices.md) | Retrieves a specific Invoice object. |
| GET | `/isirs/(isir)` | show | [ISIR](models/isirs.md) | Retrieves a specific Isir object. |
| GET | `/itemcategories` | index | [BookstoreBookstoreItemCategory](models/categories.md) | Retrieves all BookstoreBookstoreItemCategory objects. |
| GET | `/itemcategories/(bookstoreitemcategory)` | show | [BookstoreBookstoreItemCategory](models/categories.md) | Retrieves a specific BookstoreBookstoreItemCategory object. |
| GET | `/items` | index | [BookstoreItem](models/items.md) | Retrieves all BookstoreItem objects that match given filter conditions. |
| GET | `/items/(bookstoreitem)` | show | [BookstoreItem](models/items.md) | Retrieves a specific BookstoreItem object. |
| GET | `/leads` | index | [Lead](models/leads.md) | Retrieves all Lead objects that match given filter conditions. |
| GET | `/leads/(lead)` | show | [Lead](models/leads.md) | Retrieves a specific Lead object. |
| GET | `/leadsources` | index | [LeadSource](models/leadsources.md) | Retrieves all LeadSource objects. |
| GET | `/leadsources/(leadsource)` | show | [LeadSource](models/leadsources.md) | Retrieves a specific LeadSource object. |
| GET | `/ledgerentries` | index | [LedgerEntry](models/ledgers.md) | Retrieves all LedgerEntry objects that match given filter conditions. |
| GET | `/ledgerentries/(ledgerentry)` | show | [LedgerEntry](models/ledgers.md) | Retrieves a specific LedgerEntry object. |
| GET | `/letters/(letter)` | show | [Letter](models/letters.md) | Retrieves a specific Letter object. |
| GET | `/lettertemplates` | index | [LetterTemplate](models/lettertemplates.md) | Retrieves all LetterTemplate objects. |
| GET | `/lettertemplates/(lettertemplate)` | show | [LetterTemplate](models/lettertemplates.md) | Retrieves a specific LetterTemplate object. |
| GET | `/libraryresources` | index | [LibraryResource](models/libraryresources.md) | Retrieves all LibraryResource objects that match given filter conditions. |
| GET | `/libraryresources/(libraryresource)` | show | [LibraryResource](models/libraryresources.md) | Retrieves a specific LibraryResource object. |
| GET | `/libraryresources/fields` | library_fields | [LibraryResource](models/libraryresources.md) |  |
| GET | `/lmssync/run` | Run LMS sync | [ChangeLog](models/account.md) | Begin a sync operation between Populi and an outside LMS (e.g. |
| GET | `/localizations` | index | [Localization](models/localizations.md) | Retrieves all Localization objects. |
| GET | `/localizations/(localization)` | show | [Localization](models/localizations.md) | Retrieves a specific Localization object. |
| GET | `/lockareas` | index | [LockArea](models/lockareas.md) | Retrieves all LockArea objects. |
| GET | `/locktypes` | index | [LockType](models/locktypes.md) | Retrieves all LockType objects. |
| GET | `/locktypes/(locktype)` | show | [LockType](models/locktypes.md) | Retrieves a specific LockType object. |
| GET | `/logins` | logins | [ChangeLog](models/account.md) | Results are limited to logins in the past 12 months. |
| GET | `/ltitools` | index | [LtiTool](models/ltitools.md) | Retrieves all global LTI tools in the account. |
| GET | `/ltitools/(ltitool)` | show | [LtiTool](models/ltitools.md) | Retrieves a specific global LTI tool. |
| GET | `/mailinglists` | index | [MailingList](models/mailinglists.md) | Retrieves all MailingList objects. |
| GET | `/mailinglists/(mailinglist)` | show | [MailingList](models/mailinglists.md) | Retrieves a specific MailingList object. |
| GET | `/mealplans` | index | [MealPlan](models/mealplans.md) | Retrieves all MealPlan objects. |
| GET | `/mealplans/(mealplan)` | show | [MealPlan](models/mealplans.md) | Retrieves a specific MealPlan object. |
| GET | `/news` | index | [News](models/news.md) | Retrieves all News objects that match given filter conditions. |
| GET | `/news/(news)` | show | [News](models/news.md) | Retrieves a specific News object. |
| GET | `/occupations` | index | [Occupation](models/occupations.md) | Retrieves all Occupation objects. |
| GET | `/occupations/(occupation)` | show | [Occupation](models/occupations.md) | Retrieves a specific Occupation object. |
| GET | `/onlinepayments` | index | [OnlinePayment](models/onlinepayments.md) | Retrieves all OnlinePayment objects that match given filter conditions. |
| GET | `/onlinepayments/(onlinepayment)` | show | [OnlinePayment](models/onlinepayments.md) | Retrieves a specific OnlinePayment object. |
| GET | `/onlinereferences/(onlinereference)` | show_online_reference | [Application](models/applications.md) |  |
| GET | `/orders` | index | [BookstoreOrder](models/orders.md) | Retrieves all BookstoreOrder objects that match given filter conditions. |
| GET | `/orders/(bookstoreorder)` | show | [BookstoreOrder](models/orders.md) | Retrieves a specific BookstoreOrder object. |
| GET | `/organizationcustominfofields` | index (organization) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the organization type. |
| GET | `/organizationcustominfofields/(organizationcustominfofield)` | show (organization) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the organization type. |
| GET | `/organizationdomains` | index | [OrganizationDomain](models/organizationdomains.md) | Retrieves all OrganizationDomain objects. |
| GET | `/organizationdomains/(organizationdomain)` | show | [OrganizationDomain](models/organizationdomains.md) | Retrieves a specific OrganizationDomain object. |
| GET | `/organizations` | index | [Organization](models/contactorganizations.md) | Retrieves all Organization objects that match given filter conditions. |
| POST | `/organizations` | create | [Organization](models/contactorganizations.md) | Creates a new Organization object. |
| DELETE | `/organizations/(organization)` | delete | [Organization](models/contactorganizations.md) | Deletes an existing Organization object. |
| GET | `/organizations/(organization)` | show | [Organization](models/contactorganizations.md) | Retrieves a specific Organization object. |
| PUT | `/organizations/(organization)` | update | [Organization](models/contactorganizations.md) | Updates an existing Organization object. |
| GET | `/organizations/(organization)/addresses` | index (organization) | [Address](models/addresses.md) | Retrieves all Address objects tied to a specific Organization. |
| POST | `/organizations/(organization)/addresses` | create (organization) | [Address](models/addresses.md) | Creates a new Address object. |
| DELETE | `/organizations/(organization)/addresses/(address)` | delete (organization) | [Address](models/addresses.md) | Deletes an existing Address object. |
| GET | `/organizations/(organization)/addresses/(address)` | show (organization) | [Address](models/addresses.md) | Retrieves a specific Address object. |
| PUT | `/organizations/(organization)/addresses/(address)` | update (organization) | [Address](models/addresses.md) | Updates an existing Address object. |
| GET | `/organizations/(organization)/custominfodata` | index (organization) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Organization, tied to a specified Organization object. |
| POST | `/organizations/(organization)/custominfodata` | create (organization) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, tied to a specified Organization object. |
| DELETE | `/organizations/(organization)/custominfodata/(custominfodata)` | delete (organization) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, tied to a specified Organization object. |
| GET | `/organizations/(organization)/custominfodata/(custominfodata)` | show (organization) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, tied to a specified Organization object. |
| PUT | `/organizations/(organization)/custominfodata/(custominfodata)` | update (organization) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, tied to a specified Organization object. |
| GET | `/organizations/(organization)/emailaddresses` | index (organization) | [EmailAddress](models/emailaddresses.md) | Retrieves all EmailAddress objects tied to a specific Organization. |
| POST | `/organizations/(organization)/emailaddresses` | create (organization) | [EmailAddress](models/emailaddresses.md) | Creates a new EmailAddress object. |
| DELETE | `/organizations/(organization)/emailaddresses/(emailaddress)` | delete (organization) | [EmailAddress](models/emailaddresses.md) | Deletes an existing EmailAddress object. |
| GET | `/organizations/(organization)/emailaddresses/(emailaddress)` | show (organization) | [EmailAddress](models/emailaddresses.md) | Retrieves a specific EmailAddress object. |
| PUT | `/organizations/(organization)/emailaddresses/(emailaddress)` | update (organization) | [EmailAddress](models/emailaddresses.md) | Updates an existing EmailAddress object. |
| GET | `/organizations/(organization)/notes` | index (organization) | [Note](models/notes.md) | Retrieves all Note objects tied to a specific Organization. |
| POST | `/organizations/(organization)/notes` | create (organization) | [Note](models/notes.md) | Creates a new Note object. |
| GET | `/organizations/(organization)/phonenumbers` | index (organization) | [PhoneNumber](models/phonenumbers.md) | Retrieves all PhoneNumber objects tied to a specific Organization. |
| POST | `/organizations/(organization)/phonenumbers` | create (organization) | [PhoneNumber](models/phonenumbers.md) | Creates a new PhoneNumber object. |
| DELETE | `/organizations/(organization)/phonenumbers/(phonenumber)` | delete (organization) | [PhoneNumber](models/phonenumbers.md) | Deletes an existing PhoneNumber object. |
| GET | `/organizations/(organization)/phonenumbers/(phonenumber)` | show (organization) | [PhoneNumber](models/phonenumbers.md) | Retrieves a specific PhoneNumber object. |
| PUT | `/organizations/(organization)/phonenumbers/(phonenumber)` | update (organization) | [PhoneNumber](models/phonenumbers.md) | Updates an existing PhoneNumber object. |
| GET | `/organizations/(organization)/tags` | index (organization) | [Tag](models/tags.md) | Retrieves all Tag objects tied to a specific Organization. |
| GET | `/organizations/(organization)/tags/add` | add (organization) | [Tag](models/tags.md) |  |
| GET | `/organizations/(organization)/tags/remove` | remove (organization) | [Tag](models/tags.md) |  |
| GET | `/organizations/(organization)/websites` | index (organization) | [Website](models/websites.md) | Retrieves all Website objects tied to a specific Organization. |
| GET | `/organizations/deleted` | deleted | [Organization](models/contactorganizations.md) | Retrieves records that were deleted up to 180 days ago. |
| GET | `/organizationtypes` | index | [OrganizationType](models/contactorganizationtypes.md) | Retrieves all OrganizationType objects. |
| GET | `/organizationtypes/(organizationtype)` | show | [OrganizationType](models/contactorganizationtypes.md) | Retrieves a specific OrganizationType object. |
| GET | `/paymentdeadlines` | index | [PaymentDeadline](models/paymentdeadlines.md) | Retrieves all PaymentDeadline objects that match given filter conditions. |
| GET | `/paymentdeadlines/(paymentdeadline)` | show | [PaymentDeadline](models/paymentdeadlines.md) | Retrieves a specific PaymentDeadline object. |
| GET | `/paymentperiods` | index | [PaymentPeriod](models/paymentperiods.md) | Retrieves all PaymentPeriod objects that match given filter conditions. |
| GET | `/paymentperiods/(paymentperiod)` | show | [PaymentPeriod](models/paymentperiods.md) | Retrieves a specific PaymentPeriod object. |
| GET | `/paymentplans` | index | [PaymentPlan](models/paymentplans.md) | Retrieves all PaymentPlan objects. |
| GET | `/paymentplans/(paymentplan)` | show | [PaymentPlan](models/paymentplans.md) | Retrieves a specific PaymentPlan object. |
| GET | `/payments` | index | [Payment](models/payments.md) | Retrieves all Payment objects that match given filter conditions. |
| GET | `/payments/(payment)` | show | [Payment](models/payments.md) | Retrieves a specific Payment object. |
| GET | `/payments/recurring` | recurring | [Payment](models/payments.md) |  |
| GET | `/pendingcharges` | index | [PendingCharge](models/pendingcharges.md) | Retrieves all PendingCharge objects that match given filter conditions. |
| GET | `/pendingcharges/(pendingcharge)` | show | [PendingCharge](models/pendingcharges.md) | Retrieves a specific PendingCharge object. |
| GET | `/people` | index | [Person](models/people.md) | Retrieves all Person objects that match given filter conditions. |
| POST | `/people` | create | [Person](models/people.md) | Creates a new Person object. |
| DELETE | `/people/(person)` | delete | [Person](models/people.md) | Deletes an existing Person object. |
| GET | `/people/(person)` | show | [Person](models/people.md) | Retrieves a specific Person object. |
| PUT | `/people/(person)` | update | [Person](models/people.md) | Updates an existing Person object. |
| GET | `/people/(person)/addresses` | index (person) | [Address](models/addresses.md) | Retrieves all Address objects tied to a specific Person. |
| POST | `/people/(person)/addresses` | create (person) | [Address](models/addresses.md) | Creates a new Address object. |
| DELETE | `/people/(person)/addresses/(address)` | delete (person) | [Address](models/addresses.md) | Deletes an existing Address object. |
| GET | `/people/(person)/addresses/(address)` | show (person) | [Address](models/addresses.md) | Retrieves a specific Address object. |
| PUT | `/people/(person)/addresses/(address)` | update (person) | [Address](models/addresses.md) | Updates an existing Address object. |
| GET | `/people/(person)/addresses/set` | set | [Address](models/addresses.md) | Creates an address OR updates it if it already exists. |
| GET | `/people/(person)/advisors` | index | [StudentAdvisor](models/studentadvisors.md) | Retrieves all StudentAdvisor objects tied to a specific Person. |
| POST | `/people/(person)/advisors` | create | [StudentAdvisor](models/studentadvisors.md) | Creates a new StudentAdvisor object. |
| DELETE | `/people/(person)/advisors/(studentadvisor)` | delete | [StudentAdvisor](models/studentadvisors.md) | Deletes an existing StudentAdvisor object. |
| GET | `/people/(person)/aidapplications` | index (person) | [AidApplication](models/aidapplications.md) | Retrieves all AidApplication objects tied to a specific Person. |
| POST | `/people/(person)/aidapplications` | create | [AidApplication](models/aidapplications.md) | Creates a new AidApplication object. |
| DELETE | `/people/(person)/aidapplications/(aidapplication)` | delete | [AidApplication](models/aidapplications.md) | Deletes an existing AidApplication object. |
| GET | `/people/(person)/aidapplications/(aidapplication)` | show | [AidApplication](models/aidapplications.md) | Retrieves a specific AidApplication object. |
| PUT | `/people/(person)/aidapplications/(aidapplication)` | update | [AidApplication](models/aidapplications.md) | Updates an existing AidApplication object. |
| GET | `/people/(person)/aidauthorizations/` | index | [AidStudentAuthorization](models/aidstudentauthorizations.md) | Retrieves all AidStudentAuthorization objects tied to a specific Person. |
| POST | `/people/(person)/aidawards` | create | [AidAward](models/aidawards.md) | Creates a new AidAward object. |
| GET | `/people/(person)/aidawards/` | index_by_student | [AidAward](models/aidawards.md) |  |
| DELETE | `/people/(person)/aidawards/(aidaward)` | delete | [AidAward](models/aidawards.md) | Deletes an existing AidAward object. |
| GET | `/people/(person)/aidawards/(aidaward)` | show | [AidAward](models/aidawards.md) | Retrieves a specific AidAward object. |
| PUT | `/people/(person)/aidawards/(aidaward)` | update | [AidAward](models/aidawards.md) | Updates an existing AidAward object. |
| GET | `/people/(person)/aidawards/(aidaward)/disbursements` | index_by_award | [AidDisbursement](models/aiddisbursements.md) |  |
| POST | `/people/(person)/aidawards/(aidaward)/disbursements` | create (disbursement) | [AidDisbursement](models/aiddisbursements.md) | Creates a new AidDisbursement object. |
| DELETE | `/people/(person)/aidawards/(aidaward)/disbursements/(aiddisbursement)` | delete (disbursement) | [AidDisbursement](models/aiddisbursements.md) | Deletes an existing AidDisbursement object. |
| GET | `/people/(person)/aidawards/(aidaward)/disbursements/(aiddisbursement)` | show (disbursement) | [AidDisbursement](models/aiddisbursements.md) | Retrieves a specific AidDisbursement object. |
| PUT | `/people/(person)/aidawards/(aidaward)/disbursements/(aiddisbursement)` | update (disbursement) | [AidDisbursement](models/aiddisbursements.md) | Updates an existing AidDisbursement object. |
| GET | `/people/(person)/aidawards/(aidaward)/disbursements/(aiddisbursement)/post` | post | [AidDisbursement](models/aiddisbursements.md) |  |
| POST | `/people/(person)/aidawards/(aidaward)/refunds` | create (refund) | [AidDisbursement](models/aiddisbursements.md) | Creates a new AidDisbursement object. |
| DELETE | `/people/(person)/aidawards/(aidaward)/refunds/(aiddisbursement)` | delete (refund) | [AidDisbursement](models/aiddisbursements.md) | Deletes an existing AidDisbursement object. |
| GET | `/people/(person)/aidawards/(aidaward)/refunds/(aiddisbursement)` | show (refund) | [AidDisbursement](models/aiddisbursements.md) | Retrieves a specific AidDisbursement object. |
| PUT | `/people/(person)/aidawards/(aidaward)/refunds/(aiddisbursement)` | update (refund) | [AidDisbursement](models/aiddisbursements.md) | Updates an existing AidDisbursement object. |
| GET | `/people/(person)/applications` | index (by person) | [Application](models/applications.md) | Retrieves all Application objects tied to a specific Person. |
| GET | `/people/(person)/balances` | balances (person) | [Student](models/students.md) |  |
| GET | `/people/(person)/campuses` | index | [StudentCampus](models/studentcampuses.md) | Retrieves all StudentCampus objects tied to a specific Person. |
| POST | `/people/(person)/campuses` | create | [StudentCampus](models/studentcampuses.md) | Creates a new StudentCampus object. |
| DELETE | `/people/(person)/campuses/(studentcampus)` | delete | [StudentCampus](models/studentcampuses.md) | Deletes an existing StudentCampus object. |
| GET | `/people/(person)/campuses/(studentcampus)` | show | [StudentCampus](models/studentcampuses.md) | Retrieves a specific StudentCampus object. |
| DELETE | `/people/(person)/citizenships` | delete | [Citizenship](models/personcitizenships.md) | Removes all citizenship data about a person. |
| GET | `/people/(person)/citizenships` | index | [Citizenship](models/personcitizenships.md) | Retrieves all Citizenship objects tied to a specific Person. |
| POST | `/people/(person)/citizenships` | create | [Citizenship](models/personcitizenships.md) | Creates a new Citizenship object. |
| GET | `/people/(person)/communicationplans` | index | [CommunicationPlanInstance](models/communicationplaninstances.md) | Retrieves all CommunicationPlanInstance objects tied to a specific Person. |
| POST | `/people/(person)/communicationplans` | create | [CommunicationPlanInstance](models/communicationplaninstances.md) | Creates a new CommunicationPlanInstance object. |
| DELETE | `/people/(person)/communicationplans/(communicationplaninstance)` | delete | [CommunicationPlanInstance](models/communicationplaninstances.md) | Deletes an existing CommunicationPlanInstance object. |
| GET | `/people/(person)/communicationplans/(communicationplaninstance)` | show | [CommunicationPlanInstance](models/communicationplaninstances.md) | Retrieves a specific CommunicationPlanInstance object. |
| PUT | `/people/(person)/communicationplans/(communicationplaninstance)` | update | [CommunicationPlanInstance](models/communicationplaninstances.md) | Updates an existing CommunicationPlanInstance object. |
| GET | `/people/(person)/consequences` | index (by person) | [StudentConsequence](models/studentconsequences.md) | Retrieves all StudentConsequence objects tied to a specific Person. |
| GET | `/people/(person)/consequences/(studentconsequence)` | show | [StudentConsequence](models/studentconsequences.md) | Retrieves a specific StudentConsequence object. |
| GET | `/people/(person)/custominfodata` | index (person) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Person, tied to a specified Person object. |
| POST | `/people/(person)/custominfodata` | create (person) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, tied to a specified Person object. |
| DELETE | `/people/(person)/custominfodata/(custominfodata)` | delete (person) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/(custominfodata)` | show (person) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, tied to a specified Person object. |
| PUT | `/people/(person)/custominfodata/(custominfodata)` | update (person) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/admissions` | index (admissions) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Person, of the admissions type, tied to a specified Person object. |
| POST | `/people/(person)/custominfodata/admissions` | create (admissions) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, of the admissions type, tied to a specified Person object. |
| DELETE | `/people/(person)/custominfodata/admissions/(custominfodata)` | delete (admissions) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, of the admissions type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/admissions/(custominfodata)` | show (admissions) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, of the admissions type, tied to a specified Person object. |
| PUT | `/people/(person)/custominfodata/admissions/(custominfodata)` | update (admissions) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, of the admissions type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/campuslife` | index (campus life) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Person, of the campus life type, tied to a specified Person object. |
| POST | `/people/(person)/custominfodata/campuslife` | create (campus life) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, of the campus life type, tied to a specified Person object. |
| DELETE | `/people/(person)/custominfodata/campuslife/(custominfodata)` | delete (campus life) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, of the campus life type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/campuslife/(custominfodata)` | show (campus life) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, of the campus life type, tied to a specified Person object. |
| PUT | `/people/(person)/custominfodata/campuslife/(custominfodata)` | update (campus life) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, of the campus life type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/financial` | index (financial) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Person, of the financial type, tied to a specified Person object. |
| POST | `/people/(person)/custominfodata/financial` | create (financial) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, of the financial type, tied to a specified Person object. |
| DELETE | `/people/(person)/custominfodata/financial/(custominfodata)` | delete (financial) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, of the financial type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/financial/(custominfodata)` | show (financial) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, of the financial type, tied to a specified Person object. |
| PUT | `/people/(person)/custominfodata/financial/(custominfodata)` | update (financial) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, of the financial type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/financialaid` | index (financial aid) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Person, of the financial aid type, tied to a specified Person object. |
| POST | `/people/(person)/custominfodata/financialaid` | create (financial aid) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, of the financial aid type, tied to a specified Person object. |
| DELETE | `/people/(person)/custominfodata/financialaid/(custominfodata)` | delete (financial aid) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, of the financial aid type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/financialaid/(custominfodata)` | show (financial aid) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, of the financial aid type, tied to a specified Person object. |
| PUT | `/people/(person)/custominfodata/financialaid/(custominfodata)` | update (financial aid) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, of the financial aid type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/set` | generic_set | [CustomInfoData](models/custominfodata.md) | Creates a custom field value OR updates it if it already exists. |
| GET | `/people/(person)/custominfodata/student` | index (student) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Person, of the student type, tied to a specified Person object. |
| POST | `/people/(person)/custominfodata/student` | create (student) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, of the student type, tied to a specified Person object. |
| DELETE | `/people/(person)/custominfodata/student/(custominfodata)` | delete (student) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, of the student type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/student/(custominfodata)` | show (student) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, of the student type, tied to a specified Person object. |
| PUT | `/people/(person)/custominfodata/student/(custominfodata)` | update (student) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, of the student type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/term/(academicterm)` | index (term student) | [CustomInfoData](models/custominfodata.md) | Retrieves all CustomInfoData objects tied to a specific Person, of the term student type, tied to a specified Person object. |
| POST | `/people/(person)/custominfodata/term/(academicterm)` | create (term student) | [CustomInfoData](models/custominfodata.md) | Creates a new CustomInfoData object, of the term student type, tied to a specified Person object. |
| DELETE | `/people/(person)/custominfodata/term/(academicterm)/(custominfodata)` | delete (term student) | [CustomInfoData](models/custominfodata.md) | Deletes an existing CustomInfoData object, of the term student type, tied to a specified Person object. |
| GET | `/people/(person)/custominfodata/term/(academicterm)/(custominfodata)` | show (term student) | [CustomInfoData](models/custominfodata.md) | Retrieves a specific CustomInfoData object, of the term student type, tied to a specified Person object. |
| PUT | `/people/(person)/custominfodata/term/(academicterm)/(custominfodata)` | update (term student) | [CustomInfoData](models/custominfodata.md) | Updates an existing CustomInfoData object, of the term student type, tied to a specified Person object. |
| GET | `/people/(person)/defaulttuitionschedules` | index | [StudentDefaultTuitionSchedule](models/studentdefaulttuitionschedules.md) | Retrieves all StudentDefaultTuitionSchedule objects tied to a specific Person. |
| DELETE | `/people/(person)/defaulttuitionschedules/(studentdefaulttuitionschedule)` | delete | [StudentDefaultTuitionSchedule](models/studentdefaulttuitionschedules.md) | Deletes an existing StudentDefaultTuitionSchedule object. |
| GET | `/people/(person)/defaulttuitionschedules/(studentdefaulttuitionschedule)` | show | [StudentDefaultTuitionSchedule](models/studentdefaulttuitionschedules.md) | Retrieves a specific StudentDefaultTuitionSchedule object. |
| PUT | `/people/(person)/defaulttuitionschedules/create` | update | [StudentDefaultTuitionSchedule](models/studentdefaulttuitionschedules.md) | Updates an existing StudentDefaultTuitionSchedule object. |
| GET | `/people/(person)/degreeaudit` | degree_audit | [Student](models/students.md) |  |
| GET | `/people/(person)/degrees` | index | [StudentDegree](models/studentdegrees.md) | Retrieves all StudentDegree objects tied to a specific Person. |
| POST | `/people/(person)/degrees` | create | [StudentDegree](models/studentdegrees.md) | Creates a new StudentDegree object. |
| DELETE | `/people/(person)/degrees/(studentdegree)` | delete | [StudentDegree](models/studentdegrees.md) | Deletes an existing StudentDegree object. |
| GET | `/people/(person)/degrees/(studentdegree)` | show | [StudentDegree](models/studentdegrees.md) | Retrieves a specific StudentDegree object. |
| PUT | `/people/(person)/degrees/(studentdegree)` | update | [StudentDegree](models/studentdegrees.md) | Updates an existing StudentDegree object. |
| GET | `/people/(person)/degrees/(studentdegree)/specializations` | index | [StudentSpecialization](models/studentspecializations.md) | Retrieves all StudentSpecialization objects tied to a specific Person. |
| POST | `/people/(person)/degrees/(studentdegree)/specializations` | create | [StudentSpecialization](models/studentspecializations.md) | Creates a new StudentSpecialization object. |
| DELETE | `/people/(person)/degrees/(studentdegree)/specializations/(studentspecialization)` | delete | [StudentSpecialization](models/studentspecializations.md) | Deletes an existing StudentSpecialization object. |
| GET | `/people/(person)/degrees/(studentdegree)/specializations/(studentspecialization)` | show | [StudentSpecialization](models/studentspecializations.md) | Retrieves a specific StudentSpecialization object. |
| PUT | `/people/(person)/degrees/(studentdegree)/specializations/(studentspecialization)` | update | [StudentSpecialization](models/studentspecializations.md) | Updates an existing StudentSpecialization object. |
| GET | `/people/(person)/deposits` | deposits (person) | [Student](models/students.md) |  |
| GET | `/people/(person)/deposits/apply` | apply | [FinancialTransaction](models/financialtransactions.md) |  |
| GET | `/people/(person)/discipline` | index | [Discipline](models/discipline.md) | Retrieves all Discipline objects tied to a specific Person. |
| POST | `/people/(person)/discipline` | create | [Discipline](models/discipline.md) | Creates a new Discipline object. |
| DELETE | `/people/(person)/discipline/(discipline)` | delete | [Discipline](models/discipline.md) | Deletes an existing Discipline object. |
| GET | `/people/(person)/discipline/(discipline)` | show | [Discipline](models/discipline.md) | Retrieves a specific Discipline object. |
| PUT | `/people/(person)/discipline/(discipline)` | update | [Discipline](models/discipline.md) | Updates an existing Discipline object. |
| GET | `/people/(person)/emailaddresses` | index (person) | [EmailAddress](models/emailaddresses.md) | Retrieves all EmailAddress objects tied to a specific Person. |
| POST | `/people/(person)/emailaddresses` | create (person) | [EmailAddress](models/emailaddresses.md) | Creates a new EmailAddress object. |
| DELETE | `/people/(person)/emailaddresses/(emailaddress)` | delete (person) | [EmailAddress](models/emailaddresses.md) | Deletes an existing EmailAddress object. |
| GET | `/people/(person)/emailaddresses/(emailaddress)` | show (person) | [EmailAddress](models/emailaddresses.md) | Retrieves a specific EmailAddress object. |
| PUT | `/people/(person)/emailaddresses/(emailaddress)` | update (person) | [EmailAddress](models/emailaddresses.md) | Updates an existing EmailAddress object. |
| GET | `/people/(person)/emailaddresses/set` | set | [EmailAddress](models/emailaddresses.md) | Creates an email address OR updates it if it already exists. |
| GET | `/people/(person)/enrollments` | enrollments | [Student](models/students.md) |  |
| POST | `/people/(person)/enrollments` | create | [Enrollment](models/coursestudents.md) | Creates a new Enrollment object. |
| DELETE | `/people/(person)/enrollments/(enrollment)` | delete | [Enrollment](models/coursestudents.md) | Deletes an existing Enrollment object. |
| GET | `/people/(person)/enrollments/(enrollment)` | show (person) | [Enrollment](models/coursestudents.md) | Retrieves a specific Enrollment object. |
| PUT | `/people/(person)/enrollments/(enrollment)` | update | [Enrollment](models/coursestudents.md) | Updates an existing Enrollment object. |
| GET | `/people/(person)/export_transcript` | export_transcript | [Student](models/students.md) | To generate using the built-in PDF layout, set print_layout_id to PDF. |
| GET | `/people/(person)/flags` | index | [StudentFlag](models/studentflags.md) | Retrieves all StudentFlag objects tied to a specific Person. |
| GET | `/people/(person)/flags/(studentflag)` | show | [StudentFlag](models/studentflags.md) | Retrieves a specific StudentFlag object. |
| GET | `/people/(person)/gradereport` | export_grade_report | [Student](models/students.md) |  |
| GET | `/people/(person)/honors` | index | [StudentHonor](models/studenthonors.md) | Retrieves all StudentHonor objects tied to a specific Person. |
| POST | `/people/(person)/honors` | create | [StudentHonor](models/studenthonors.md) | Creates a new StudentHonor object. |
| DELETE | `/people/(person)/honors/(studenthonor)` | delete | [StudentHonor](models/studenthonors.md) | Deletes an existing StudentHonor object. |
| GET | `/people/(person)/honors/(studenthonor)` | show | [StudentHonor](models/studenthonors.md) | Retrieves a specific StudentHonor object. |
| GET | `/people/(person)/idcard` | Export (person) | [IDCardTemplate](models/idcardtemplates.md) | Either id_card_template_id or print_layout_id is required. |
| GET | `/people/(person)/leads` | index (person) | [Lead](models/leads.md) | Retrieves all Lead objects tied to a specific Person. |
| POST | `/people/(person)/leads` | create | [Lead](models/leads.md) | Creates a new Lead object. |
| DELETE | `/people/(person)/leads/(lead)` | delete | [Lead](models/leads.md) | Deletes an existing Lead object. |
| GET | `/people/(person)/leads/(lead)` | show (person) | [Lead](models/leads.md) | Retrieves a specific Lead object. |
| PUT | `/people/(person)/leads/(lead)` | update | [Lead](models/leads.md) | Updates an existing Lead object. |
| GET | `/people/(person)/locks` | index (person) | [LockStudent](models/locks.md) | Retrieves all LockStudent objects tied to a specific Person. |
| GET | `/people/(person)/locks/(lockstudent)` | show | [LockStudent](models/locks.md) | Retrieves a specific LockStudent object. |
| GET | `/people/(person)/locks/(lockstudent)/delete` | delete_lock | [LockStudent](models/locks.md) |  |
| PUT | `/people/(person)/locks/(lockstudent)/update` | update_lock | [LockStudent](models/locks.md) | Updates the lock attribute of an existing LockStudent object. |
| GET | `/people/(person)/locks/create` | create_lock | [LockStudent](models/locks.md) |  |
| POST | `/people/(person)/mark_deceased` | mark_deceased | [Person](models/people.md) |  |
| GET | `/people/(person)/mealplans` | index | [MealPlanStudent](models/mealplanstudents.md) | Retrieves all MealPlanStudent objects tied to a specific Person. |
| POST | `/people/(person)/mealplans` | create | [MealPlanStudent](models/mealplanstudents.md) | Creates a new MealPlanStudent object. |
| DELETE | `/people/(person)/mealplans/(mealplanstudent)` | delete | [MealPlanStudent](models/mealplanstudents.md) | Deletes an existing MealPlanStudent object. |
| GET | `/people/(person)/mealplans/(mealplanstudent)` | show | [MealPlanStudent](models/mealplanstudents.md) | Retrieves a specific MealPlanStudent object. |
| PUT | `/people/(person)/mealplans/(mealplanstudent)` | update | [MealPlanStudent](models/mealplanstudents.md) | Updates an existing MealPlanStudent object. |
| GET | `/people/(person)/notes` | index (person) | [Note](models/notes.md) | Retrieves all Note objects tied to a specific Person. |
| POST | `/people/(person)/notes` | create (person) | [Note](models/notes.md) | Creates a new Note object. |
| GET | `/people/(person)/onlinepaymentlink` | get_online_payment_link | [Student](models/students.md) |  |
| GET | `/people/(person)/organizations` | index | [OrganizationMember](models/contactorganizationmembers.md) | Retrieves all OrganizationMember objects tied to a specific Person. |
| POST | `/people/(person)/organizations` | create | [OrganizationMember](models/contactorganizationmembers.md) | Creates a new OrganizationMember object. |
| DELETE | `/people/(person)/organizations/(organizationmember)` | delete | [OrganizationMember](models/contactorganizationmembers.md) | Deletes an existing OrganizationMember object. |
| GET | `/people/(person)/organizations/(organizationmember)` | show | [OrganizationMember](models/contactorganizationmembers.md) | Retrieves a specific OrganizationMember object. |
| PUT | `/people/(person)/organizations/(organizationmember)` | update | [OrganizationMember](models/contactorganizationmembers.md) | Updates an existing OrganizationMember object. |
| GET | `/people/(person)/paymentplans` | index | [PaymentPlanStudent](models/paymentplanstudents.md) | Retrieves all PaymentPlanStudent objects tied to a specific Person. |
| POST | `/people/(person)/paymentplans` | create | [PaymentPlanStudent](models/paymentplanstudents.md) | Creates a new PaymentPlanStudent object. |
| DELETE | `/people/(person)/paymentplans/(paymentplanstudent)` | delete | [PaymentPlanStudent](models/paymentplanstudents.md) | Deletes an existing PaymentPlanStudent object. |
| GET | `/people/(person)/paymentplans/(paymentplanstudent)` | show | [PaymentPlanStudent](models/paymentplanstudents.md) | Retrieves a specific PaymentPlanStudent object. |
| GET | `/people/(person)/payments` | index (person) | [Payment](models/payments.md) | Retrieves all Payment objects tied to a specific Person. |
| POST | `/people/(person)/payments` | create | [Payment](models/payments.md) | Creates a new Payment object. |
| GET | `/people/(person)/payments/(payment)` | show (person) | [Payment](models/payments.md) | Retrieves a specific Payment object. |
| GET | `/people/(person)/pendingcharges` | index (person) | [PendingCharge](models/pendingcharges.md) | Retrieves all PendingCharge objects tied to a specific Person. |
| POST | `/people/(person)/pendingcharges` | create | [PendingCharge](models/pendingcharges.md) | Creates a new PendingCharge object. |
| POST | `/people/(person)/pendingcharges/invoice` | invoice | [PendingCharge](models/pendingcharges.md) |  |
| GET | `/people/(person)/phonenumbers` | index (person) | [PhoneNumber](models/phonenumbers.md) | Retrieves all PhoneNumber objects tied to a specific Person. |
| POST | `/people/(person)/phonenumbers` | create (person) | [PhoneNumber](models/phonenumbers.md) | Creates a new PhoneNumber object. |
| DELETE | `/people/(person)/phonenumbers/(phonenumber)` | delete (person) | [PhoneNumber](models/phonenumbers.md) | Deletes an existing PhoneNumber object. |
| GET | `/people/(person)/phonenumbers/(phonenumber)` | show (person) | [PhoneNumber](models/phonenumbers.md) | Retrieves a specific PhoneNumber object. |
| PUT | `/people/(person)/phonenumbers/(phonenumber)` | update (person) | [PhoneNumber](models/phonenumbers.md) | Updates an existing PhoneNumber object. |
| GET | `/people/(person)/phonenumbers/(phonenumber)/unverify` | unverify (person) | [PhoneNumber](models/phonenumbers.md) |  |
| GET | `/people/(person)/phonenumbers/set` | set | [PhoneNumber](models/phonenumbers.md) | Creates a phone number OR updates it if it already exists. |
| GET | `/people/(person)/portal_links` | portal_links | [Person](models/people.md) |  |
| GET | `/people/(person)/posts` | index (person) | [Post](models/bulletinboardposts.md) | Retrieves all Post objects tied to a specific Person. |
| GET | `/people/(person)/posts/(post)` | show (person) | [Post](models/bulletinboardposts.md) | Retrieves a specific Post object. |
| GET | `/people/(person)/programs` | index | [StudentProgram](models/studentprograms.md) | Retrieves all StudentProgram objects tied to a specific Person. |
| POST | `/people/(person)/programs` | create | [StudentProgram](models/studentprograms.md) | Creates a new StudentProgram object. |
| DELETE | `/people/(person)/programs/(studentprogram)` | delete | [StudentProgram](models/studentprograms.md) | Deletes an existing StudentProgram object. |
| PUT | `/people/(person)/programs/(studentprogram)` | update | [StudentProgram](models/studentprograms.md) | Updates an existing StudentProgram object. |
| DELETE | `/people/(person)/races` | delete | [PersonRace](models/personraces.md) | Removes all race and ethnicity information about a person. |
| GET | `/people/(person)/races` | index | [PersonRace](models/personraces.md) | Retrieves all PersonRace objects tied to a specific Person. |
| POST | `/people/(person)/races` | create | [PersonRace](models/personraces.md) | Creates a new PersonRace object. |
| GET | `/people/(person)/relationships` | index | [PersonRelationship](models/personrelationships.md) | Retrieves all PersonRelationship objects tied to a specific Person. |
| POST | `/people/(person)/relationships` | create | [PersonRelationship](models/personrelationships.md) | Creates a new PersonRelationship object. |
| DELETE | `/people/(person)/relationships/(personrelationship)` | delete | [PersonRelationship](models/personrelationships.md) | Deletes an existing PersonRelationship object. |
| GET | `/people/(person)/relationships/(personrelationship)` | show | [PersonRelationship](models/personrelationships.md) | Retrieves a specific PersonRelationship object. |
| PUT | `/people/(person)/relationships/(personrelationship)` | update | [PersonRelationship](models/personrelationships.md) | Updates an existing PersonRelationship object. |
| GET | `/people/(person)/requirementexceptions` | index | [RequirementException](models/requirementexceptions.md) | Retrieves all RequirementException objects tied to a specific Person. |
| POST | `/people/(person)/restore` | restore | [Person](models/people.md) |  |
| GET | `/people/(person)/roles` | index (person) | [Role](models/roles.md) | Retrieves all Role objects tied to a specific Person. |
| GET | `/people/(person)/roles/add` | add (person) | [Role](models/roles.md) | If the role already exists for this person, but is inactive, this route will reactivate it. |
| GET | `/people/(person)/roles/deactivate` | deactivate (person) | [Role](models/roles.md) |  |
| GET | `/people/(person)/roles/remove` | remove (person) | [Role](models/roles.md) | Note: The Student role should typically not be removed if the person in question has academic data. |
| GET | `/people/(person)/roomplans` | index | [RoomPlanStudent](models/roomplanstudents.md) | Retrieves all RoomPlanStudent objects tied to a specific Person. |
| POST | `/people/(person)/roomplans` | create | [RoomPlanStudent](models/roomplanstudents.md) | Creates a new RoomPlanStudent object. |
| DELETE | `/people/(person)/roomplans/(roomplanstudent)` | delete | [RoomPlanStudent](models/roomplanstudents.md) | Deletes an existing RoomPlanStudent object. |
| GET | `/people/(person)/roomplans/(roomplanstudent)` | show | [RoomPlanStudent](models/roomplanstudents.md) | Retrieves a specific RoomPlanStudent object. |
| PUT | `/people/(person)/roomplans/(roomplanstudent)` | update | [RoomPlanStudent](models/roomplanstudents.md) | Updates an existing RoomPlanStudent object. |
| GET | `/people/(person)/sapoverrides` | index | [SAPOverride](models/sapoverrides.md) | Retrieves all SAPOverride objects tied to a specific Person. |
| GET | `/people/(person)/sapoverrides/(sapoverride)` | show | [SAPOverride](models/sapoverrides.md) | Retrieves a specific SAPOverride object. |
| GET | `/people/(person)/schedule/(academicterm)` | show_schedule | [Student](models/students.md) |  |
| GET | `/people/(person)/standardizedtestscores` | index (by person) | [StandardizedTestScore](models/standardizedtestscores.md) | Retrieves all StandardizedTestScore objects tied to a specific Person. |
| POST | `/people/(person)/standardizedtestscores` | create | [StandardizedTestScore](models/standardizedtestscores.md) | Creates a new StandardizedTestScore object. |
| DELETE | `/people/(person)/standardizedtestscores/(standardizedtestscore)` | delete | [StandardizedTestScore](models/standardizedtestscores.md) | Deletes an existing StandardizedTestScore object. |
| GET | `/people/(person)/standardizedtestscores/(standardizedtestscore)` | show | [StandardizedTestScore](models/standardizedtestscores.md) | Retrieves a specific StandardizedTestScore object. |
| PUT | `/people/(person)/standardizedtestscores/(standardizedtestscore)` | update | [StandardizedTestScore](models/standardizedtestscores.md) | Updates an existing StandardizedTestScore object. |
| GET | `/people/(person)/standardizedtestscores/(standardizedtestscore)/sections` | index | [StandardizedTestSectionScore](models/standardizedtestsectionscores.md) | Retrieves all StandardizedTestSectionScore objects tied to a specific Person. |
| POST | `/people/(person)/standardizedtestscores/(standardizedtestscore)/sections` | create | [StandardizedTestSectionScore](models/standardizedtestsectionscores.md) | Creates a new StandardizedTestSectionScore object. |
| DELETE | `/people/(person)/standardizedtestscores/(standardizedtestscore)/sections/(standardizedtestsectionscore)` | delete | [StandardizedTestSectionScore](models/standardizedtestsectionscores.md) | Deletes an existing StandardizedTestSectionScore object. |
| GET | `/people/(person)/standardizedtestscores/(standardizedtestscore)/sections/(standardizedtestsectionscore)` | show | [StandardizedTestSectionScore](models/standardizedtestsectionscores.md) | Retrieves a specific StandardizedTestSectionScore object. |
| PUT | `/people/(person)/standardizedtestscores/(standardizedtestscore)/sections/(standardizedtestsectionscore)` | update | [StandardizedTestSectionScore](models/standardizedtestsectionscores.md) | Updates an existing StandardizedTestSectionScore object. |
| GET | `/people/(person)/student` | show | [Student](models/students.md) | Retrieves a specific Student object. |
| PUT | `/people/(person)/student/update` | update | [Student](models/students.md) | Updates an existing Student object. |
| GET | `/people/(person)/tags` | index (person) | [Tag](models/tags.md) | Retrieves all Tag objects tied to a specific Person. |
| GET | `/people/(person)/tags/add` | add (person) | [Tag](models/tags.md) |  |
| GET | `/people/(person)/tags/remove` | remove (person) | [Tag](models/tags.md) |  |
| GET | `/people/(person)/termsettings` | index | [AcademicTermPersonSettings](models/academictermpersonsettings.md) | Retrieves all AcademicTermPersonSettings objects tied to a specific Person. |
| GET | `/people/(person)/termsettings/(academicterm)` | show | [AcademicTermPersonSettings](models/academictermpersonsettings.md) | Retrieves a specific AcademicTermPersonSettings object. |
| GET | `/people/(person)/transcript` | transcript | [Student](models/students.md) | This route will return a lot of student data, the structure of which is too complex to articulate here. |
| GET | `/people/(person)/transcriptnotes` | transcript_notes | [Student](models/students.md) |  |
| GET | `/people/(person)/transfercredits` | index | [TransferCredit](models/transfercredits.md) | Retrieves all TransferCredit objects tied to a specific Person. |
| GET | `/people/(person)/transferinstitutions` | index | [TransferInstitution](models/transferinstitutions.md) | Retrieves all TransferInstitution objects tied to a specific Person. |
| POST | `/people/(person)/transferinstitutions` | create | [TransferInstitution](models/transferinstitutions.md) | Creates a new TransferInstitution object. |
| DELETE | `/people/(person)/transferinstitutions/(transferinstitution)` | delete | [TransferInstitution](models/transferinstitutions.md) | Deletes an existing TransferInstitution object. |
| GET | `/people/(person)/transferinstitutions/(transferinstitution)` | show | [TransferInstitution](models/transferinstitutions.md) | Retrieves a specific TransferInstitution object. |
| PUT | `/people/(person)/transferinstitutions/(transferinstitution)` | update | [TransferInstitution](models/transferinstitutions.md) | Updates an existing TransferInstitution object. |
| POST | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits` | create | [TransferCredit](models/transfercredits.md) | Creates a new TransferCredit object. |
| DELETE | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)` | delete | [TransferCredit](models/transfercredits.md) | Deletes an existing TransferCredit object. |
| GET | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)` | show | [TransferCredit](models/transfercredits.md) | Retrieves a specific TransferCredit object. |
| PUT | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)` | update | [TransferCredit](models/transfercredits.md) | Updates an existing TransferCredit object. |
| GET | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)/programs` | index | [TransferCreditProgram](models/transfercreditprograms.md) | Retrieves all TransferCreditProgram objects tied to a specific Person. |
| POST | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)/programs` | create | [TransferCreditProgram](models/transfercreditprograms.md) | Creates a new TransferCreditProgram object. |
| DELETE | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)/programs/(transfercreditprogram)` | delete | [TransferCreditProgram](models/transfercreditprograms.md) | Deletes an existing TransferCreditProgram object. |
| GET | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)/programs/(transfercreditprogram)` | show | [TransferCreditProgram](models/transfercreditprograms.md) | Retrieves a specific TransferCreditProgram object. |
| PUT | `/people/(person)/transferinstitutions/(transferinstitution)/transfercredits/(transfercredit)/programs/(transfercreditprogram)` | update | [TransferCreditProgram](models/transfercreditprograms.md) | Updates an existing TransferCreditProgram object. |
| GET | `/people/(person)/tuitionschedules` | index | [TuitionScheduleStudent](models/tuitionschedulestudents.md) | Retrieves all TuitionScheduleStudent objects tied to a specific Person. |
| POST | `/people/(person)/tuitionschedules` | create | [TuitionScheduleStudent](models/tuitionschedulestudents.md) | Creates a new TuitionScheduleStudent object. |
| DELETE | `/people/(person)/tuitionschedules/(tuitionschedulestudent)` | delete | [TuitionScheduleStudent](models/tuitionschedulestudents.md) | Deletes an existing TuitionScheduleStudent object. |
| GET | `/people/(person)/tuitionschedules/(tuitionschedulestudent)` | show | [TuitionScheduleStudent](models/tuitionschedulestudents.md) | Retrieves a specific TuitionScheduleStudent object. |
| PUT | `/people/(person)/tuitionschedules/(tuitionschedulestudent)` | update | [TuitionScheduleStudent](models/tuitionschedulestudents.md) | Updates an existing TuitionScheduleStudent object. |
| POST | `/people/(person)/update_profile_picture` | update_profile_picture | [Person](models/people.md) | Updates the profile_picture attribute of an existing Person object. |
| POST | `/people/(person)/upload_file` | upload_file | [Person](models/people.md) |  |
| GET | `/people/(person)/violations` | index (by person) | [StudentViolation](models/studentviolations.md) | Retrieves all StudentViolation objects tied to a specific Person. |
| GET | `/people/(person)/violations/(studentviolation)` | show | [StudentViolation](models/studentviolations.md) | Retrieves a specific StudentViolation object. |
| GET | `/people/(person)/websites` | index (person) | [Website](models/websites.md) | Retrieves all Website objects tied to a specific Person. |
| GET | `/people/by_student_id` | by_student_id | [Person](models/people.md) | Get a single person by their visible student ID rather than their Populi ID. |
| GET | `/people/deleted` | deleted | [Person](models/people.md) | Retrieves records that were deleted up to 180 days ago. |
| GET | `/people/possibleduplicates` | possible_duplicates | [Person](models/people.md) |  |
| GET | `/personbalances` | balances (index) | [Student](models/students.md) |  |
| GET | `/personcustominfofields` | index (person) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the person type. |
| GET | `/personcustominfofields/(personcustominfofield)` | show (person) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the person type. |
| GET | `/populiinvoices` | index | [PopuliInvoice](models/populiinvoice.md) | These are invoices sent to your school monthly for using Populi. |
| GET | `/populiinvoices/(populiinvoice)` | show | [PopuliInvoice](models/populiinvoice.md) | Retrieves a specific PopuliInvoice object. |
| GET | `/populipayments` | index | [PopuliPayment](models/populipayment.md) | These are payments your school made to pay for their monthly use of Populi. |
| GET | `/populipayments/(populipayment)` | show | [PopuliPayment](models/populipayment.md) | Retrieves a specific PopuliPayment object. |
| GET | `/printlayouts` | index | [PrintLayout](models/printlayouts.md) | Retrieves all PrintLayout objects. |
| GET | `/printlayouts/(printlayout)` | show | [PrintLayout](models/printlayouts.md) | Retrieves a specific PrintLayout object. |
| GET | `/printlayouttypes` | types | [PrintLayout](models/printlayouts.md) |  |
| GET | `/programs` | index | [Program](models/programs.md) | Retrieves all Program objects. |
| GET | `/programs/(program)` | show | [Program](models/programs.md) | Retrieves a specific Program object. |
| GET | `/programs/(program)/students` | students | [Program](models/programs.md) |  |
| GET | `/programs/(program)/transfercreditsgradeoptions` | transfer_credit_grade_options | [Program](models/programs.md) |  |
| GET | `/races` | index | [Race](models/races.md) | Retrieves all Race objects. |
| GET | `/races/(race)` | show | [Race](models/races.md) | Retrieves a specific Race object. |
| GET | `/refundpolicies` | index | [RefundPolicy](models/refundpolicies.md) | Retrieves all RefundPolicy objects. |
| GET | `/refundpolicies/(refundpolicy)` | show | [RefundPolicy](models/refundpolicies.md) | Retrieves a specific RefundPolicy object. |
| GET | `/refunds/(refund)` | show | [Refund](models/refunds.md) | Retrieves a specific Refund object. |
| GET | `/relationshiptypes` | index | [RelationshipType](models/relationshiptypes.md) | Retrieves all RelationshipType objects. |
| GET | `/relationshiptypes/(relationshiptype)` | show | [RelationshipType](models/relationshiptypes.md) | Retrieves a specific RelationshipType object. |
| GET | `/returnreasons` | index | [ReturnReason](models/returnreasons.md) | Retrieves all ReturnReason objects. |
| GET | `/returnreasons/(returnreason)` | show | [ReturnReason](models/returnreasons.md) | Retrieves a specific ReturnReason object. |
| GET | `/roles` | index | [Role](models/roles.md) | Retrieves all Role objects. |
| GET | `/roles/(role)` | show | [Role](models/roles.md) | Retrieves a specific Role object. |
| GET | `/roles/(role)/members` | members | [Role](models/roles.md) |  |
| GET | `/roomplans` | index | [RoomPlan](models/roomplans.md) | Retrieves all RoomPlan objects. |
| GET | `/roomplans/(roomplan)` | show | [RoomPlan](models/roomplans.md) | Retrieves a specific RoomPlan object. |
| GET | `/rooms` | index | [Room](models/rooms.md) | Retrieves all Room objects. |
| GET | `/rooms/(room)` | show | [Room](models/rooms.md) | Retrieves a specific Room object. |
| GET | `/rooms/schedule` | schedule | [Room](models/rooms.md) | This method returns a week's worth of room schedule data, equivalent to the Campus Life -> Facilities Schedule. |
| GET | `/rubrics` | index | [Rubric](models/rubrics.md) | Retrieves all Rubric objects. |
| GET | `/rubrics/(rubric)` | show | [Rubric](models/rubrics.md) | Retrieves a specific Rubric object. |
| GET | `/salesreceipts` | index | [SalesReceipt](models/salesreceipts.md) | Retrieves all SalesReceipt objects that match given filter conditions. |
| GET | `/salesreceipts/(salesreceipt)` | show | [SalesReceipt](models/salesreceipts.md) | Retrieves a specific SalesReceipt object. |
| GET | `/sappolicies` | index | [SAPPolicy](models/sappolicies.md) | Retrieves all SAPPolicy objects. |
| GET | `/sappolicies/(sappolicy)` | show | [SAPPolicy](models/sappolicies.md) | Retrieves a specific SAPPolicy object. |
| GET | `/shippingmethods` | index | [ShippingMethod](models/shippingmethods.md) | Retrieves all ShippingMethod objects. |
| GET | `/shippingmethods/(shippingmethod)` | show | [ShippingMethod](models/shippingmethods.md) | Retrieves a specific ShippingMethod object. |
| GET | `/specializationtypes` | index | [SpecializationType](models/specializationtypes.md) | Retrieves all SpecializationType objects. |
| GET | `/specializationtypes/(specializationtype)` | show | [SpecializationType](models/specializationtypes.md) | Retrieves a specific SpecializationType object. |
| GET | `/standardizedtests` | index | [StandardizedTest](models/standardizedtests.md) | Retrieves all StandardizedTest objects. |
| GET | `/standardizedtests/(standardizedtest)` | show | [StandardizedTest](models/standardizedtests.md) | Retrieves a specific StandardizedTest object. |
| GET | `/standardizedtestscores` | index (by test) | [StandardizedTestScore](models/standardizedtestscores.md) | Retrieves all StandardizedTestScore objects that match given filter conditions. |
| GET | `/studentcustominfofields` | index (student) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the student type. |
| GET | `/studentcustominfofields/(studentcustominfofield)` | show (student) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the student type. |
| GET | `/tags` | index | [Tag](models/tags.md) | Retrieves all Tag objects. |
| POST | `/tags` | create | [Tag](models/tags.md) | If you try to create a Tag that already exists (same name), the existing Tag object will be returned. |
| DELETE | `/tags/(tag)` | delete | [Tag](models/tags.md) | Custom tags can be deleted. |
| GET | `/tags/(tag)` | show | [Tag](models/tags.md) | Retrieves a specific Tag object. |
| GET | `/termstudentcustominfofields` | index (term student) | [CustomInfoField](models/custominfofield.md) | Retrieves all CustomInfoField objects, of the term student type. |
| GET | `/termstudentcustominfofields/(termstudentcustominfofield)` | show (term student) | [CustomInfoField](models/custominfofield.md) | Retrieves a specific CustomInfoField object, of the term student type. |
| GET | `/timezone` | timezone | [Utilities](models/utilities.md) | Get the timezone of your school. |
| GET | `/todos` | index | [Todo](models/todos.md) | Retrieves all Todo objects that match given filter conditions. |
| POST | `/todos` | create | [Todo](models/todos.md) | Creates a new Todo object. |
| DELETE | `/todos/(todo)` | delete | [Todo](models/todos.md) | Deletes an existing Todo object. |
| GET | `/todos/(todo)` | show | [Todo](models/todos.md) | Retrieves a specific Todo object. |
| POST | `/todos/(todo)/complete` | complete | [Todo](models/todos.md) |  |
| GET | `/todotemplates` | index | [TodoTemplate](models/todotemplates.md) | Retrieves all TodoTemplate objects. |
| GET | `/todotemplates/(todotemplate)` | show | [TodoTemplate](models/todotemplates.md) | Retrieves a specific TodoTemplate object. |
| GET | `/transactions` | index | [FinancialTransaction](models/financialtransactions.md) | Retrieves all FinancialTransaction objects that match given filter conditions. |
| GET | `/transactions/(financialtransaction)` | show | [FinancialTransaction](models/financialtransactions.md) | Retrieves a specific FinancialTransaction object. |
| GET | `/transactions/(financialtransaction)/repost` | repost | [FinancialTransaction](models/financialtransactions.md) |  |
| GET | `/transactions/(financialtransaction)/reverse` | reverse | [FinancialTransaction](models/financialtransactions.md) |  |
| GET | `/transactions/(financialtransaction)/void` | void | [FinancialTransaction](models/financialtransactions.md) |  |
| GET | `/transcriptrequestdeliverymethods` | index | [TranscriptRequestDeliveryMethod](models/transcriptrequestdeliverymethods.md) | Retrieves all TranscriptRequestDeliveryMethod objects. |
| GET | `/transcriptrequestdeliverymethods/(transcriptrequestdeliverymethod)` | show | [TranscriptRequestDeliveryMethod](models/transcriptrequestdeliverymethods.md) | Retrieves a specific TranscriptRequestDeliveryMethod object. |
| GET | `/transcriptrequestfeerules` | index | [TranscriptRequestFeeRule](models/transcriptrequestfeerules.md) | Retrieves all TranscriptRequestFeeRule objects. |
| GET | `/transcriptrequestfeerules/(transcriptrequestfeerule)` | show | [TranscriptRequestFeeRule](models/transcriptrequestfeerules.md) | Retrieves a specific TranscriptRequestFeeRule object. |
| GET | `/transcriptrequests` | index | [TranscriptRequest](models/transcriptrequests.md) | Retrieves all TranscriptRequest objects that match given filter conditions. |
| GET | `/transcriptrequests/(transcriptrequest)` | show | [TranscriptRequest](models/transcriptrequests.md) | Retrieves a specific TranscriptRequest object. |
| GET | `/transfercredits` | index (transfercredit) | [TransferCredit](models/transfercredits.md) | Retrieves all TransferCredit objects that match given filter conditions. |
| GET | `/tuitionschedules` | index | [TuitionSchedule](models/tuitionschedules.md) | Retrieves all TuitionSchedule objects. |
| GET | `/tuitionschedules/(tuitionschedule)` | show | [TuitionSchedule](models/tuitionschedules.md) | Retrieves a specific TuitionSchedule object. |
| GET | `/users` | index | [User](models/users.md) | Retrieves all User objects that match given filter conditions. |
| POST | `/users/(person)` | create | [User](models/users.md) | Creates a new User object. |
| DELETE | `/users/(user)` | delete | [User](models/users.md) | Deletes an existing User object. |
| GET | `/users/(user)` | show | [User](models/users.md) | Retrieves a specific User object. |
| POST | `/users/(user)/block` | block | [User](models/users.md) |  |
| GET | `/users/(user)/enable_external_email_account` | enable_external_email_account | [User](models/users.md) | If your school is using the Google integration, this will trigger a matching system email account to be created on the Google side for a Us… |
| GET | `/users/(user)/hard_delete` | hard_delete_user | [User](models/users.md) | Permanently delete a user account so the username can be re-assigned. |
| POST | `/users/(user)/unblock` | unblock | [User](models/users.md) |  |
| GET | `/users/deleted` | deleted | [User](models/users.md) | Retrieves records that were deleted up to 180 days ago. |
| GET | `/violations` | index | [Violation](models/violations.md) | Retrieves all Violation objects. |
| GET | `/violations/(violation)` | show | [Violation](models/violations.md) | Retrieves a specific Violation object. |
| GET | `/webhooks/examples/:trigger_abbrv` | show example webhook payload | [Utilities](models/utilities.md) | This method returns an example JSON payload of a Webhook coming from Populi triggered by a specified type of Automation. |
