# The use of this code is under my permission
# If you use this code without my consent, you must pay me 100 bucks.

import asyncio
import time 
import random as r
from typing import NoReturn, Literal
from colorama import Fore, Style

Gender = Literal["Man", "Woman"]


class NoSocialization(Exception):
    """This error occurs when nick tries to socialize"""
    def __init__(self, gender: Gender) -> None:
        message = "Stop Getting Freaky" if gender == "Woman" else "Can't socialize"
        super().__init__(message)


class NickWhite:
    """Nick White class"""
    def __init__(self, *, high_ego: bool, age: int) -> None:
        self.high_ego = high_ego
        self.age = age
        self.last_age = r.randint(age, 100)
    
    def meet_drake(self) -> None:
        """Nick White meets Drake!"""
        if not self.high_ego:
            self.high_ego = True 
        else:
            self.high_ego = float("inf")

        return None 
    
    @property
    def is_alive(self) -> bool:
        return self.age <= self.last_age
    
    def sleep(self) -> None:
        print("Dreaming ...")
        time.sleep(5)
        print("Woke up!")
        return None 
    
    def get_freaky(self) -> None:
        """Nick White gets freaky with an OF model"""
        print("You are the CSS to my html code")
    
    async def stream(self, long: float) -> None: 
        print(f"{Fore.BLUE} streaming now! {Fore.RESET}")
        await asyncio.gather(
            self.roast(long),
            self.code(long)
        )
        
    async def socialize(self, person: Gender) -> NoReturn: 
        """Nick White cannot socialize"""
        raise NoSocialization(person)


    async def roast(self, long: float) -> None: 
        print("Haha! Fucking Loser (roasting)")
        await asyncio.sleep(long)
        print("I am never tired of roasting")

    async def code(self, long: float) -> None: 
        print("Nick White is coding (for his job)")
        await asyncio.sleep(long)
        self.sleep()

    async def start_life(self) -> None:
        while self.is_alive:
            await self.stream(5)
            self.age += 1
            print(f"{Fore.YELLOW}NICK WHITE's birthday! I am {self.age} years old {Style.RESET_ALL}")

            try:
                person: Gender = r.choice(["Man", "Woman"])
                await self.socialize(person)
            except NoSocialization as s:

                print(f"{Fore.RED}{s}{Style.RESET_ALL}")
            
            self.get_freaky()
            print("\n\n")
        
        print(f"{Fore.CYAN}NICK WHITE PASSED AWAY AT {self.last_age} years old {Style.RESET_ALL}")


if __name__ == "__main__":
    nw = NickWhite(high_ego=True, age=31)
    asyncio.run(nw.start_life())
