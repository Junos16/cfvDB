import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity('Card') 
export class CardEntity {
    @PrimaryGeneratedColumn()
    cardId: number;

    @Column()
    title: string;
    
    @Column()
    name: string; // Fix the typo here
}
