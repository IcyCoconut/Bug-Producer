using System;
using System.Collections;
using System.Collections.Generic;

namespace CompSim{
    class Player{
        public string name;
        public string[] stats = {"all", "hp", "attack_dmg"};
        private int hp;
        private int attack_dmg;
        
        public Player(string name, int init_hp, int init_ad){
            this.name = name;
            this.hp = init_hp;
            this.attack_dmg = init_ad;
        }

        public void attack(Player target){
            target.take_dmg(this.attack_dmg);
        }

        public void take_dmg(int dmg){
            this.hp -= dmg;
        }

        public bool is_dead(){
            return this.hp <= 0;
        }

        public int get_hp(){
            return this.hp;
        }

        public int get_attack_dmg(){
            return this.attack_dmg;
        }

        public void set_status(string mode, int new_hp = 0, int new_dmg = 0){
            if (string.IsNullOrEmpty(mode)){
                throw NullReferenceException("mode must given");
            }

            bool mode_valid = false;
            foreach (string s in this.stats){
                if (s == mode){
                    mode_valid = true;
                    break;
                }
            }
            if (!mode_valid){
                throw Exception("mode is not valid, mode should be an element in Player.stats.");
            }

            if (mode == "all" || mode == "hp"){
                this.hp = new_hp;
            }
            if (mode == "all" || mode == "attack_dmg"){
                this.attack_dmg = new_dmg;
            }
        }

        public void print_status(){
            Console.WriteLine("- {0:d}:\t{1:d}", "hp", this.hp);
            Console.WriteLine("- {0:d}:\t{1:d}", "damage", this.attack_dmg);
        }
    }

    class Simulator{

        private ArrayList players = new ArrayList();

        int count = 0;

        public Simulator(){
        }

        public Simulator(Player player){
            this.players.Add(player);
        }

        public Simulator(Player player1, Player player2){
            this.players.Add(player1);
            this.players.Add(player2);
        }

        public Simulator(Player[] player_list){
            foreach (Player p in player_list){
                this.players.Add(p);
            }
        }

        public void add_player(Player player){
            this.players.Add(player);
        }

        public void round_step(){
            Console.WriteLine("Round: {0:d}", ++count);
            
            this.players[0].attack(this.players[1]);
            this.players[1].attack(this.players[0]);
            this.players[0].print_status();
            this.players[1].print_status();
        }
    }

    class Main_func{
        public static void Main(string[] args){
            Player pA = new Player("A", 100, 10);
            Player pB = new Player("B", 100, 15);

            Simulator game = new Simulator(pA);
            game.add_player(pB);

            game.round_step();
        }
    }
}