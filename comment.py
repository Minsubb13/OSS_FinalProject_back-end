from fastapi import APIRouter, Path
from model import Comment

comment_router = APIRouter()

comment_list = []

@comment_router.post("/comment")
async def add_comment(comment: Comment) -> dict:
    comment.id = len(comment_list) + 1
    comment_list.append(comment)
    return {
        "msg": "visiter's comments added successfully",
        "comment": comment
    }

@comment_router.get("/comment")
async def retrieve_comments() -> dict:
    return {
        "comments": comment_list
    }

@comment_router.get("/comment/{comment_id}")
async def get_single_comment(comment_id: str = Path(..., title="the ID of the comment to retrieve")) -> dict:
    for comment in comment_list:
        if comment.id == comment_id:
            return {"visiter's comments": comment}
    return {"msg": "visiter's comments with supplied ID doesn't exist"}

@comment_router.delete("/comment/{comment_id}")
async def delete_comment(comment_id: int = Path(..., title="the ID of the comment to delete")) -> dict:
    for index, comment in enumerate(comment_list):
        if comment.id == comment_id:
            del comment_list[index]
            return {"message": f"Comment {comment_id} deleted successfully"}
    return {"message": "Comment not found"}