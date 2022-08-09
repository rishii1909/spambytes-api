
from rest_framework.response import Response

CREATE_SUCCESS = Response({"success": True, "Message":"User Created Successfully"})
UPDATE_SUCCESS = Response({"success": True, "Message":"User Updated Successfully"})
DELETE_SUCCESS = Response({"success": True, "Message":"User Deleted Successfully"})

FAILURE = Response({"success": False}, status=400)