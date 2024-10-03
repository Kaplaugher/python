from litestar import get, post
from typing import List
from models import Opportunity, File
from litestar.exceptions import HTTPException
import database as database
from datetime import date
import logging


@get("/opportunities")
async def get_opportunities() -> List[Opportunity]:
    try:
        mock_opportunity = Opportunity(
            id=1,
            name="Mock Project",
            description="This is a mock project for testing purposes",
            client="ACME Corporation",
            needs="Web development, API integration",
            date=str(date.today()),
            files=["mockfile1.pdf", "mockfile2.docx"]
        )
        
        return [mock_opportunity]
    except Exception as e:
        logging.error(f"Error in get_opportunities: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@get("/opportunity/{opportunity_id:int}")
async def get_opportunity(opportunity_id: int) -> Opportunity:
    opportunity = next((opp for opp in database.opportunities if opp.id == opportunity_id), None)
    if opportunity is None:
        raise ValueError("Opportunity not found")
    return opportunity

@post("/opportunities")
async def create_opportunity(opportunity: Opportunity) -> Opportunity:
    opportunity.id = len(database.opportunities) + 1
    opportunity.date = date.today()  # Set the date to today if not provided
    database.opportunities.append(opportunity)
    return opportunity

@post("/opportunity/{opportunity_id:int}/files")
async def add_files(opportunity_id: int, files: List[File]) -> Opportunity:
    opportunity = next((opp for opp in database.opportunities if opp.id == opportunity_id), None)
    if opportunity is None:
        raise ValueError("Opportunity not found")
    opportunity.files.extend(files)
    return opportunity