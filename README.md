# nestjs_a_json_to_all

Put beg.py into your nestjs project folder
## Run
ipython beg.py your_entity_name your_entity.json
## Json
your_entity.json contains the structure of your entity, it looks exactly same as the json you sent to server or responsed.

For example: 
test.json

{"name": "hi", "age": 1} 

This json will convert to a entity file like this:

test.entity.ts
```typescript
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
```
