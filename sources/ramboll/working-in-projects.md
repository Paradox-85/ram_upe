We have work packages to deliver, that in turn are broken down into smaller deliveries, where each delivery relate to one or more dicipline (diciplines can be viewed as tags).
Deliveries can be of different types, and depending on the type, they ar the object of a given process that involves a checklist, and in some cases a workflow describing the lifecycle from creatinon to delivery. Part of the workflow involve self-checks, cross discipline checks and approvals.
The authoring of the work happens across a range of dedicated tools the varies depending on the disciplines. Ideally, we could use some additional custom properties (in a process property set) in oder to persist the state of the delivery artifact during its likefcycle. Maybe we have custom add-on in each authoring tools basically embedding a similar UI based on the process state baked ino the model.
The idea is the same across the various tools.
The UI allows to mark checks, raise approval requests (via API call to a backend service), or trigger other relevant actions.


Encode our operating model in a machine-readable way in order to embedding it at various levels.
Define a fixed set of allowed types and terms? Keep it small and consistent.
type.domain.name.version?
Google's OKF format looks promising. Could it be used as a basis?
