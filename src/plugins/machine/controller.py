"""Machine controller. This module defines the API routes for the Machine plugin."""
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException, Depends, Query, Path, Security
from src.plugins.auth.firebase import verify_firebase_token_and_role, verify_firebase_token
from src.plugins.machine.repository import get_all, get_by_id, get_by_type
from src.plugins.machine.schema import Machine

router = APIRouter(prefix="/api/v1/machine", tags=["Machine"])

# list all machines
@router.get("/",status_code=201, response_model=list[Machine], summary="Get all machines in the dataset")
async def get_all_machines(user=Depends(verify_firebase_token)):
    pass
    #try:
    #    machines = await get_all()
    #    return {"machines": machines}
    #except Exception as e:
    #    print(f"Error getting all machines: {e}")
    #    #raise HTTPException(status_code=500, detail=str(e))

# filter
@router.post("/filter", response_model=list[Machine], status_code=201, summary="Filter machines by type")
async def filter_machines(user=Depends(verify_firebase_token), machine_type: str = Query(..., title="The type of the machine")):
    pass
    #try:
    #    machines = await get_by_type(machine_type)
    #    return {"machines": machines}
    #except Exception as e:
    #    raise HTTPException(status_code=500, detail=str(e))

# get machine by ID
@router.get("/{machine_id}", response_model=Machine, status_code=201, summary="Get machine by ID")
async def get_machine_by_id(
    machine_id: str = Path(..., title="The ID of the machine"),
    user=Depends(verify_firebase_token)
):
    pass
    #try:
    #    machine = await get_by_id(machine_id)
    #    return {"machine": machine}
    #except Exception as e:
    #    raise HTTPException(status_code=500, detail=str(e))

# get machine by name
@router.get("/name/{machine_name}", response_model=Machine, status_code=201, summary="Get machine by name")
async def get_machine_by_name():
    pass