from abc import ABC, abstractmethod

from starlette.requests import Request

from a2a.types import AgentCard


class AgentCardHandler(ABC):
    """Abstract base class for handling agent card requests.

    This class defines the interface for fetching agent cards
    and extended agent cards.
    """

    @abstractmethod
    async def get_agent_card(self, request: Request) -> AgentCard:
        """Handles GET requests for the agent card endpoint.

        Args:
            request: The incoming Starlette Request object.

        Returns:
            An AgentCard object.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

    @abstractmethod
    async def get_authenticated_extended_agent_car(self, request: Request) -> AgentCard | None:
        """Handles GET requests for the authenticated extended agent card endpoint.

        Args:
            request: The incoming Starlette Request object.

        Returns:
            An AgentCard object with extended capabilities.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
