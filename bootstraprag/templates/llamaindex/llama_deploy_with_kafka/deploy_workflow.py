from llama_deploy import (
    deploy_workflow,
    WorkflowServiceConfig,
    ControlPlaneConfig
)
from retry_guideline_query_engine_workflow import build_rag_workflow_with_retry_guideline_query_engine
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())


async def deploy_rag_workflow_with_retry_guideline_query_engine():
    rag_workflow = build_rag_workflow_with_retry_guideline_query_engine()
    try:
        await deploy_workflow(
            workflow=rag_workflow,
            workflow_config=WorkflowServiceConfig(
                host="127.0.0.1",
                port=8004,
                # service name matches the name of the workflow used in Agentic Workflow
                service_name="rag_workflow_with_retry_guideline_query_engine",
                description="RAG workflow",
            ),
            # Config controlled by env vars
            control_plane_config=ControlPlaneConfig()
        )
    except Exception as e:
        print(e)

if __name__ == "__main__":
    import asyncio
    import nest_asyncio

    nest_asyncio.apply()
    try:
        asyncio.run(deploy_rag_workflow_with_retry_guideline_query_engine())
    except Exception as e:
        print(e)