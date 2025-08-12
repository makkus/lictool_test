"""
__init__.py

Copyright (c) 2025 Markus Binsteiner
All rights reserved.

SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import IO, Any, Union
import builtins

"""Top-level package for the lictool_test project."""

__author__ = "Markus Binsteiner"
__email__ = "markus@frkl.dev"

try:
    from rich import inspect
    from rich import print as rich_print

    setattr(builtins, "insp", inspect)

    def dbg(
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        file: Union[IO[str], None] = None,
        flush: bool = False,
    ) -> None:
        for obj in objects:
            try:
                rich_print(obj, sep=sep, end=end, file=file, flush=flush)
            except Exception:
                rich_print(
                    f"[green]{obj}[/green]", sep=sep, end=end, file=file, flush=flush
                )

    setattr(builtins, "dbg", dbg)

except ImportError:  # Graceful fallback if Rich isn't installed.
    pass

try:
    from devtools import debug

    def DBG(
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        file: Union[IO[str], None] = None,
        flush: bool = False,
    ) -> None:
        # objs = (
        #     ["[green]----------------------------------------------[/green]"]
        #     + list(objects)
        #     + ["[green]----------------------------------------------[/green]"]
        # )
        return debug(*objects)  # type: ignore

    setattr(builtins, "DBG", DBG)
except ImportError:  # Graceful fallback if DevTools isn't installed.
    pass

try:
    from icecream import ic  # type: ignore

    setattr(builtins, "ic", ic)
except ImportError:  # Graceful fallback if IceCream isn't installed.
    pass

try:
    from wat import wat

    setattr(builtins, "wats", wat.s)
    setattr(builtins, "wat", wat)
except ImportError:  # Graceful fallback if IceCream isn't installed.
    pass

try:
    import snoop  # type: ignore

    snoop.install()
except ImportError:  # Graceful fallback if Snoop isn't installed.
    pass
