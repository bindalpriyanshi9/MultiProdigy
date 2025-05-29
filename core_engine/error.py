from .logging import logger

# ❌ Error Reporting Hook
def report_error(error: Exception):
    logger.error(f"❌ Unhandled error: {str(error)}")
    
