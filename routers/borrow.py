from fastapi import APIRouter, HTTPException
from typing import List
from schemas.borrow import BorrowRequest, ReturnRequest, BorrowRecordResponse
from services.borrow import BorrowCrud

borrow_router = APIRouter()

# Get all borrowing records
@borrow_router.get("/borrow-records", response_model=List[BorrowRecordResponse])
def get_all_borrow_records():
    try:
        return BorrowCrud.get_all_borrow_records()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve borrow records.")

# Get borrow records for a specific user
@borrow_router.get("/borrow-records/{user_id}", response_model=List[BorrowRecordResponse])
def get_user_borrow_records(user_id: int):
    try:
        return BorrowCrud.get_borrow_records_by_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve borrow records for user.")

# Borrow a book
@borrow_router.post("/borrow-book/")
async def borrow_book(request: BorrowRequest):
    try:
        response = BorrowCrud.borrow_book(request.book_id, request.user_id)
        return {"message": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Return a book
@borrow_router.post("/return-book/")
async def return_book(request: ReturnRequest):
    try:
        response = BorrowCrud.return_book(request.book_id, request.user_id)
        return {"message": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
