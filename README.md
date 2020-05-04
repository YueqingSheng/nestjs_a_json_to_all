# nestjs_a_json_to_all

## Put beg.py into your nestjs project folder
## Run
ipython beg.py your_entity_name your_entity.json

your_entity.json contains the structure of your entity, it looks exactly same as the json you sent to server or responsed
For example: {"name": "hi", "age": 1} , this json will convert to a entity file like this:
export class Test {
        @PrimaryGeneratedColumn()
        @ApiModelProperty()
        id: number;

        @Column()
        @ApiModelProperty()
        name: string;

        @Column()
        @ApiModelProperty()
        age: number;
}
