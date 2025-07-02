import logging

from starlette.requests import Request

from a2a.server.agent_card.agent_card_handler import AgentCardHandler
from a2a.types import AgentCard


logger = logging.getLogger(__name__)


class InMemoryAgentCardHandler(AgentCardHandler):
    """An in-memory implementation of the AgentCardHandler.

    Stores the agent card and optionally an extended agent card
    in memory, serving them directly from class attributes.
    """

    def __init__(
            self,
            agent_card: AgentCard,
            extended_agent_card: AgentCard | None = None
    ):
        """Initializes the InMemoryAgentCardHandler.

        Args:
            agent_card: The AgentCard describing the agent's capabilities.
            extended_agent_card: An optional, distinct AgentCard to be served
              at the authenticated extended card endpoint.
        """
        self.agent_card = agent_card
        self.extended_agent_card = extended_agent_card
        if (
            self.agent_card.supportsAuthenticatedExtendedCard
            and self.extended_agent_card is None
        ):
            logger.error(
                'AgentCard.supportsAuthenticatedExtendedCard is True, but no extended_agent_card was provided. The /agent/authenticatedExtendedCard endpoint will return 404.'
            )

    async def get_agent_card(self, request: Request) -> AgentCard:
        """Retrieves the agent card from local memory class attribute."""
        return self.agent_card

    async def get_authenticated_extended_agent_car(self, request: Request) -> AgentCard | None:
        """Retrieves the extended agent card from local memory class attribute."""
        return self.extended_agent_card
