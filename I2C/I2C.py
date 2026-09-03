"""Platform-independent interface for FCFD I2C transports."""

from abc import ABC, abstractmethod
from typing import Optional, Tuple


class I2C(ABC):
	"""Template for an I2C transport implementation."""

	@abstractmethod
	def read(self, board_address: int, address: int, n: int) -> Tuple[int, Optional[bytes]]:
		"""Read ``n`` bytes from a register."""
		raise NotImplementedError

	@abstractmethod
	def write(self, board_address: int, address: int, data) -> bool:
		"""Write data to a register and return whether it succeeded."""
		raise NotImplementedError

	@abstractmethod
	def get_number_of_devices(self) -> int:
		"""Return the number of available I2C devices."""
		raise NotImplementedError

	@abstractmethod
	def describe_error(self, code: int) -> str:
		"""Return a human-readable description for an error code."""
		raise NotImplementedError